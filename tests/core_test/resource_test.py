"""Tests for the Resource base class."""

import pytest

from flyingcircus.core import Resource

# TODO RESOURCE_PROPERTIES is used

SIMPLE_RESOURCE_NAME = "NameSpace::Service::Resource"


class SimpleResource(Resource):
    RESOURCE_TYPE = SIMPLE_RESOURCE_NAME


class TestResourceUnusualAttributes:
    """Verify special behaviour for some attributes on a CloudFormation Resource"""

    # Type
    # ----

    def test_type_attribute_always_exists_and_is_from_class_constant(self):
        data = SimpleResource()

        assert data.Type == SIMPLE_RESOURCE_NAME

    def test_type_cannot_be_set_in_constructor(self):
        with pytest.raises(TypeError) as excinfo:
            # noinspection PyArgumentList
            _ = SimpleResource(Type="CantSetThis")

        assert "Type" in str(excinfo.value)

    def test_type_cannot_be_set_as_attribute(self):
        data = SimpleResource()

        with pytest.raises(AttributeError) as excinfo:
            data.Type = "CantSetThis"

        assert data.Type == SIMPLE_RESOURCE_NAME

    def test_type_must_be_specified_in_concrete_class(self):
        class InvalidResource(Resource):
            # RESOURCE_TYPE = "SomethingSomething
            pass

        with pytest.raises(TypeError) as excinfo:
            _ = InvalidResource()

        error_message = str(excinfo.value)
        assert "RESOURCE_TYPE" in error_message \
               and "InvalidResource" in error_message

    # Metadata
    # --------

    def test_metadata_attribute_can_be_set_and_read(self):
        data = SimpleResource()

        data.Metadata = {'foo': 'bar'}

        assert data.Metadata['foo'] == 'bar'

    def test_metadata_cannot_be_set_in_constructor(self):
        with pytest.raises(TypeError) as excinfo:
            # noinspection PyArgumentList
            _ = SimpleResource(Metadata={"CantSetThis": "Nope"})

        assert "Metadata" in str(excinfo.value)

    # Resource-Specific Attributes
    # ----------------------------

    def test_creationpolicy_cannot_be_set_on_normal_resource(self):
        data = SimpleResource()

        with pytest.raises(AttributeError) as excinfo:
            data.CreationPolicy = "CantSetThis"

        assert "CreationPolicy" in str(excinfo.value)

    def test_updatepolicy_cannot_be_set_on_normal_resource(self):
        data = SimpleResource()

        with pytest.raises(AttributeError) as excinfo:
            data.UpdatePolicy = "CantSetThis"

        assert "UpdatePolicy" in str(excinfo.value)
