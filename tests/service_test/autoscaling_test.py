"""Tests for AutoScalingGroup functionality."""

import flyingcircus
from flyingcircus.core import dedent
from flyingcircus.service.autoscaling import autoscaling_group_by_cpu
from ..validation_helper import AwsTemplateValidation


class TestCpuAutoScalingGroup:
    """Test the behaviour of a CPU-based auto-scaling group."""

    ASG_WITH_CPU_YAML = dedent(
        """
        ---
        AWSTemplateFormatVersion: '2010-09-09'
        Description: |
          Deploy an auto-scaling group that scales based on lower and upper CPU usage
          thresholds.
        Metadata:
          FlyingCircus:
            version: {}
        Resources:
          AutoScalingGroup:
            Type: AWS::AutoScaling::AutoScalingGroup
            Properties:
              AvailabilityZones:
                Fn::GetAZs: !Ref AWS::Region
              LaunchConfigurationName: !Ref LaunchConfiguration
              MaxSize: 3
              MinSize: 1
          LaunchConfiguration:
            Type: AWS::AutoScaling::LaunchConfiguration
            Properties:
              ImageId: ami-1a668878
              InstanceType: t2.micro
          ScaleDownScalingAlarm:
            Type: AWS::CloudWatch::Alarm
            Properties:
              AlarmActions:
              - !Ref ScaleDownScalingPolicy
              AlarmDescription: |-
                Alarm if CPU too low or metric disappears indicating instance is down
              ComparisonOperator: LessThanThreshold
              Dimensions:
              - Name: AutoScalingGroupName
                Value: !Ref AutoScalingGroup
              EvaluationPeriods: 1
              MetricName: CPUUtilization
              Namespace: AWS/EC2
              Period: 60
              Statistic: Average
              Threshold: 49
          ScaleDownScalingPolicy:
            Type: AWS::AutoScaling::ScalingPolicy
            Properties:
              AdjustmentType: ChangeInCapacity
              AutoScalingGroupName: !Ref AutoScalingGroup
              Cooldown: 1
              ScalingAdjustment: -1
          ScaleUpScalingAlarm:
            Type: AWS::CloudWatch::Alarm
            Properties:
              AlarmActions:
              - !Ref ScaleUpScalingPolicy
              AlarmDescription: |-
                Alarm if CPU too high or metric disappears indicating instance is down
              ComparisonOperator: GreaterThanThreshold
              Dimensions:
              - Name: AutoScalingGroupName
                Value: !Ref AutoScalingGroup
              EvaluationPeriods: 1
              MetricName: CPUUtilization
              Namespace: AWS/EC2
              Period: 60
              Statistic: Average
              Threshold: 74
          ScaleUpScalingPolicy:
            Type: AWS::AutoScaling::ScalingPolicy
            Properties:
              AdjustmentType: ChangeInCapacity
              AutoScalingGroupName: !Ref AutoScalingGroup
              Cooldown: 1
              ScalingAdjustment: 1
    """.format(
            flyingcircus.__version__
        )
    )

    def test_yaml(self):
        stack = autoscaling_group_by_cpu(low=49, high=74)

        template = stack.export("yaml")

        assert template == self.ASG_WITH_CPU_YAML


class TestValidateAutoScalingService(AwsTemplateValidation):
    """Verify that all convenience functions in the Autoscaling service module
    produce stacks that are valid.
    """

    def get_stacks_under_test(self):
        return [
            autoscaling_group_by_cpu(),
            # TODO simple_scaling_policy
        ]
