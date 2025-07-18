# coding: utf-8
# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import pytest
import unittest
from azure.communication.identity import *

class IdentifierRawIdTest(unittest.TestCase):
    def test_raw_id(self):
        _assert_raw_id(
            CommunicationUserIdentifier(
                id="8:acs:bbbcbc1e-9f06-482a-b5d8-20e3f26ef0cd_45ab2481-1c1c-4005-be24-0ffb879b1130"
            ),
            "8:acs:bbbcbc1e-9f06-482a-b5d8-20e3f26ef0cd_45ab2481-1c1c-4005-be24-0ffb879b1130",
        )
        _assert_raw_id(
            CommunicationUserIdentifier(
                id="8:gcch-acs:bbbcbc1e-9f06-482a-b5d8-20e3f26ef0cd_45ab2481-1c1c-4005-be24-0ffb879b1130"
            ),
            "8:gcch-acs:bbbcbc1e-9f06-482a-b5d8-20e3f26ef0cd_45ab2481-1c1c-4005-be24-0ffb879b1130",
        )
        _assert_raw_id(CommunicationUserIdentifier(id="someFutureFormat"), "someFutureFormat")
        _assert_raw_id(
            MicrosoftTeamsUserIdentifier(user_id="45ab2481-1c1c-4005-be24-0ffb879b1130"),
            "8:orgid:45ab2481-1c1c-4005-be24-0ffb879b1130",
        )
        _assert_raw_id(
            MicrosoftTeamsUserIdentifier(user_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="PUBLIC"),
            "8:orgid:45ab2481-1c1c-4005-be24-0ffb879b1130",
        )
        _assert_raw_id(
            MicrosoftTeamsUserIdentifier(user_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="DOD"),
            "8:dod:45ab2481-1c1c-4005-be24-0ffb879b1130",
        )
        _assert_raw_id(
            MicrosoftTeamsUserIdentifier(user_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="GCCH"),
            "8:gcch:45ab2481-1c1c-4005-be24-0ffb879b1130",
        )
        _assert_raw_id(
            MicrosoftTeamsUserIdentifier(user_id="45ab2481-1c1c-4005-be24-0ffb879b1130", is_anonymous=False),
            "8:orgid:45ab2481-1c1c-4005-be24-0ffb879b1130",
        )
        _assert_raw_id(
            MicrosoftTeamsUserIdentifier(user_id="45ab2481-1c1c-4005-be24-0ffb879b1130", is_anonymous=True),
            "8:teamsvisitor:45ab2481-1c1c-4005-be24-0ffb879b1130",
        )
        _assert_raw_id(
            MicrosoftTeamsUserIdentifier(
                user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
                raw_id="8:orgid:legacyFormat",
            ),
            "8:orgid:legacyFormat",
        )
        _assert_raw_id(
            MicrosoftTeamsAppIdentifier(app_id="45ab2481-1c1c-4005-be24-0ffb879b1130"),
            "28:orgid:45ab2481-1c1c-4005-be24-0ffb879b1130",
        )
        _assert_raw_id(
            MicrosoftTeamsAppIdentifier(app_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="PUBLIC"),
            "28:orgid:45ab2481-1c1c-4005-be24-0ffb879b1130",
        )
        _assert_raw_id(
            MicrosoftTeamsAppIdentifier(app_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="DOD"),
            "28:dod:45ab2481-1c1c-4005-be24-0ffb879b1130",
        )
        _assert_raw_id(
            MicrosoftTeamsAppIdentifier(app_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="GCCH"),
            "28:gcch:45ab2481-1c1c-4005-be24-0ffb879b1130",
        )
        _assert_raw_id(PhoneNumberIdentifier(value="+112345556789"), "4:+112345556789")
        _assert_raw_id(PhoneNumberIdentifier(value="112345556789"), "4:112345556789")
        _assert_raw_id(
            PhoneNumberIdentifier(value="+112345556789", raw_id="4:otherFormat"),
            "4:otherFormat",
        )
        _assert_raw_id(
            PhoneNumberIdentifier(value="otherFormat", raw_id="4:207ffef6-9444-41fb-92ab-20eacaae2768"),
            "4:207ffef6-9444-41fb-92ab-20eacaae2768",
        )
        # cspell:disable
        _assert_raw_id(
            PhoneNumberIdentifier(
                value="otherFormat",
                raw_id="4:207ffef6-9444-41fb-92ab-20eacaae2768_207ffef6-9444-41fb-92ab-20eacaae2768",
            ),
            "4:207ffef6-9444-41fb-92ab-20eacaae2768_207ffef6-9444-41fb-92ab-20eacaae2768",
        )
        _assert_raw_id(
            PhoneNumberIdentifier(
                value="otherFormat",
                raw_id="4:+112345556789_207ffef6-9444-41fb-92ab-20eacaae2768",
            ),
            "4:+112345556789_207ffef6-9444-41fb-92ab-20eacaae2768",
        )
        _assert_raw_id(
            TeamsExtensionUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
            tenant_id="tenant123",
            resource_id="resource123",
            cloud="PUBLIC"
            ),
            "8:acs:resource123_tenant123_45ab2481-1c1c-4005-be24-0ffb879b1130",
        )
        _assert_raw_id(
            TeamsExtensionUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
            tenant_id="tenant123",
            resource_id="resource123",
            cloud="DOD"
            ),
            "8:dod-acs:resource123_tenant123_45ab2481-1c1c-4005-be24-0ffb879b1130",
        )
        _assert_raw_id(
            TeamsExtensionUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
            tenant_id="tenant123",
            resource_id="resource123",
            cloud="GCCH"
            ),
            "8:gcch-acs:resource123_tenant123_45ab2481-1c1c-4005-be24-0ffb879b1130",
        )
        _assert_raw_id(
            TeamsExtensionUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
            tenant_id="tenant123",
            resource_id="resource123",
            cloud="PUBLIC",
            raw_id="8:extension:legacyFormat"
            ),
            "8:extension:legacyFormat",
        )
        
    def test_identifier_from_raw_id(self):
        _assert_communication_identifier(
            "8:acs:bbbcbc1e-9f06-482a-b5d8-20e3f26ef0cd_45ab2481-1c1c-4005-be24-0ffb879b1130",
            CommunicationUserIdentifier(
                id="8:acs:bbbcbc1e-9f06-482a-b5d8-20e3f26ef0cd_45ab2481-1c1c-4005-be24-0ffb879b1130"
            ),
        )
        _assert_communication_identifier(
            "8:spool:bbbcbc1e-9f06-482a-b5d8-20e3f26ef0cd_45ab2481-1c1c-4005-be24-0ffb879b1130",
            CommunicationUserIdentifier(
                id="8:spool:bbbcbc1e-9f06-482a-b5d8-20e3f26ef0cd_45ab2481-1c1c-4005-be24-0ffb879b1130"
            ),
        )
        _assert_communication_identifier(
            "8:dod-acs:bbbcbc1e-9f06-482a-b5d8-20e3f26ef0cd_45ab2481-1c1c-4005-be24-0ffb879b1130",
            CommunicationUserIdentifier(
                id="8:dod-acs:bbbcbc1e-9f06-482a-b5d8-20e3f26ef0cd_45ab2481-1c1c-4005-be24-0ffb879b1130"
            ),
        )
        _assert_communication_identifier(
            "8:gcch-acs:bbbcbc1e-9f06-482a-b5d8-20e3f26ef0cd_45ab2481-1c1c-4005-be24-0ffb879b1130",
            CommunicationUserIdentifier(
                id="8:gcch-acs:bbbcbc1e-9f06-482a-b5d8-20e3f26ef0cd_45ab2481-1c1c-4005-be24-0ffb879b1130"
            ),
        )
        _assert_communication_identifier("8:acs:something", CommunicationUserIdentifier(id="8:acs:something"))
        _assert_communication_identifier(
            "8:orgid:45ab2481-1c1c-4005-be24-0ffb879b1130",
            MicrosoftTeamsUserIdentifier(user_id="45ab2481-1c1c-4005-be24-0ffb879b1130"),
        )
        _assert_communication_identifier(
            "8:orgid:45ab2481-1c1c-4005-be24-0ffb879b1130",
            MicrosoftTeamsUserIdentifier(
                user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
                cloud="PUBLIC",
                is_anonymous=False,
            ),
        )
        _assert_communication_identifier(
            "8:dod:45ab2481-1c1c-4005-be24-0ffb879b1130",
            MicrosoftTeamsUserIdentifier(
                user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
                cloud="DOD",
                is_anonymous=False,
            ),
        )
        _assert_communication_identifier(
            "8:gcch:45ab2481-1c1c-4005-be24-0ffb879b1130",
            MicrosoftTeamsUserIdentifier(
                user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
                cloud="GCCH",
                is_anonymous=False,
            ),
        )
        _assert_communication_identifier(
            "8:teamsvisitor:45ab2481-1c1c-4005-be24-0ffb879b1130",
            MicrosoftTeamsUserIdentifier(user_id="45ab2481-1c1c-4005-be24-0ffb879b1130", is_anonymous=True),
        )
        _assert_communication_identifier(
            "8:orgid:legacyFormat",
            MicrosoftTeamsUserIdentifier(user_id="legacyFormat", cloud="PUBLIC", is_anonymous=False),
        )
        _assert_communication_identifier(
            "28:orgid:45ab2481-1c1c-4005-be24-0ffb879b1130",
            MicrosoftTeamsAppIdentifier(app_id="45ab2481-1c1c-4005-be24-0ffb879b1130"),
        )
        _assert_communication_identifier(
            "28:orgid:45ab2481-1c1c-4005-be24-0ffb879b1130",
            MicrosoftTeamsAppIdentifier(app_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="PUBLIC"),
        )
        _assert_communication_identifier(
            "28:dod:45ab2481-1c1c-4005-be24-0ffb879b1130",
            MicrosoftTeamsAppIdentifier(app_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="DOD"),
        )
        _assert_communication_identifier(
            "28:gcch:45ab2481-1c1c-4005-be24-0ffb879b1130",
            MicrosoftTeamsAppIdentifier(app_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="GCCH"),
        )
        _assert_phonenumber_identifier(
            "4:+112345556789",
            PhoneNumberIdentifier(value="+112345556789"),
            withIsAnonymous=False,
            withAssertedId=False)
        _assert_phonenumber_identifier(
            "4:112345556789",
            PhoneNumberIdentifier(value="112345556789"),
            withIsAnonymous=False,
            withAssertedId=False)
        _assert_phonenumber_identifier(
            "4:otherFormat",
            PhoneNumberIdentifier(value="otherFormat"),
            withIsAnonymous=False,
            withAssertedId=False)
        _assert_phonenumber_identifier(
            "4:207ffef6-9444-41fb-92ab-20eacaae2768",
            PhoneNumberIdentifier(value="207ffef6-9444-41fb-92ab-20eacaae2768"),
            withIsAnonymous=False,
            withAssertedId=False
        )
        # cspell:disable
        _assert_phonenumber_identifier(
            "4:207ffef6-9444-41fb-92ab-20eacaae2768_207ffef6-9444-41fb-92ab-20eacaae2768",
            PhoneNumberIdentifier(value="207ffef6-9444-41fb-92ab-20eacaae2768_207ffef6-9444-41fb-92ab-20eacaae2768",
                                  raw_id="4:207ffef6-9444-41fb-92ab-20eacaae2768_207ffef6-9444-41fb-92ab-20eacaae2768"),
            withIsAnonymous=False,
            withAssertedId=True
        )
        _assert_phonenumber_identifier(
            "4:anonymous",
            PhoneNumberIdentifier(value="anonymous", raw_id="4:anonymous"),
            withIsAnonymous=True, withAssertedId=False
        )
        _assert_phonenumber_identifier(
            "4:+112345556789",
            PhoneNumberIdentifier(value="+112345556789"),
            withIsAnonymous=False,
            withAssertedId=False
        )
        _assert_communication_identifier(
            "8:acs:resource123_tenant123_45ab2481-1c1c-4005-be24-0ffb879b1130",
            TeamsExtensionUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
            tenant_id="tenant123",
            resource_id="resource123",
            cloud="PUBLIC",
            ),
        )
        _assert_communication_identifier(
            "8:dod-acs:resource123_tenant123_45ab2481-1c1c-4005-be24-0ffb879b1130",
            TeamsExtensionUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
            tenant_id="tenant123",
            resource_id="resource123",
            cloud="DOD",
            ),
        )
        _assert_communication_identifier(
            "8:gcch-acs:resource123_tenant123_45ab2481-1c1c-4005-be24-0ffb879b1130",
            TeamsExtensionUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
            tenant_id="tenant123",
            resource_id="resource123",
            cloud="GCCH",
            ),
        )
        # cspell:enable
        _assert_communication_identifier(
            "28:ag08-global:01234567-89ab-cdef-0123-456789abcdef",
            UnknownIdentifier(identifier="28:ag08-global:01234567-89ab-cdef-0123-456789abcdef"),
        )
        _assert_communication_identifier("", UnknownIdentifier(identifier=""))
        with pytest.raises(Exception):
            identifier_from_raw_id(None)

    def test_roundtrip(self):
        _assert_roundtrip("8:acs:bbbcbc1e-9f06-482a-b5d8-20e3f26ef0cd_45ab2481-1c1c-4005-be24-0ffb879b1130")
        _assert_roundtrip("8:spool:bbbcbc1e-9f06-482a-b5d8-20e3f26ef0cd_45ab2481-1c1c-4005-be24-0ffb879b1130")
        _assert_roundtrip("8:dod-acs:bbbcbc1e-9f06-482a-b5d8-20e3f26ef0cd_45ab2481-1c1c-4005-be24-0ffb879b1130")
        _assert_roundtrip("8:gcch-acs:bbbcbc1e-9f06-482a-b5d8-20e3f26ef0cd_45ab2481-1c1c-4005-be24-0ffb879b1130")
        _assert_roundtrip("8:acs:something")
        _assert_roundtrip("8:orgid:45ab2481-1c1c-4005-be24-0ffb879b1130")
        _assert_roundtrip("8:dod:45ab2481-1c1c-4005-be24-0ffb879b1130")
        _assert_roundtrip("8:gcch:45ab2481-1c1c-4005-be24-0ffb879b1130")
        _assert_roundtrip("8:teamsvisitor:45ab2481-1c1c-4005-be24-0ffb879b1130")
        _assert_roundtrip("8:orgid:legacyFormat")
        _assert_roundtrip("4:+112345556789")
        _assert_roundtrip("4:112345556789")
        _assert_roundtrip("4:otherFormat")
        _assert_roundtrip("4:anonymous")
        _assert_roundtrip("4:207ffef6-9444-41fb-92ab-20eacaae2768")
        # cspell:disable
        _assert_roundtrip("4:207ffef6-9444-41fb-92ab-20eacaae2768_207ffef6-9444-41fb-92ab-20eacaae2768")
        _assert_roundtrip("4:+112345556789_207ffef6-9444-41fb-92ab-20eacaae2768")
        # cspell:enable
        _assert_roundtrip("28:45ab2481-1c1c-4005-be24-0ffb879b1130")
        _assert_roundtrip("28:gcch-global:01234567-89ab-cdef-0123-456789abcdef")
        _assert_roundtrip("28:dod-global:01234567-89ab-cdef-0123-456789abcdef")
        _assert_roundtrip("28:orgid:01234567-89ab-cdef-0123-456789abcdef")
        _assert_roundtrip("28:gcch:01234567-89ab-cdef-0123-456789abcdef")
        _assert_roundtrip("28:dod:01234567-89ab-cdef-0123-456789abcdef")
        _assert_roundtrip("28:dod:01234567-89ab-cdef-0123-456789abcdef")
        _assert_roundtrip("")

        _assert_roundtrip("8:acs:resource123_tenant123_45ab2481-1c1c-4005-be24-0ffb879b1130")
        _assert_roundtrip("8:dod-acs:resource123_tenant123_45ab2481-1c1c-4005-be24-0ffb879b1130")
        _assert_roundtrip("8:gcch-acs:resource123_tenant123_45ab2481-1c1c-4005-be24-0ffb879b1130")

    def test_equality_based_on_raw_id(self):
        # CommunicationUserIdentifiers are equal.
        assert CommunicationUserIdentifier(
            id="8:acs:bbbcbc1e-9f06-482a-b5d8-20e3f26ef0cd_45ab2481-1c1c-4005-be24-0ffb879b1130"
        ) == CommunicationUserIdentifier(
            id="8:acs:bbbcbc1e-9f06-482a-b5d8-20e3f26ef0cd_45ab2481-1c1c-4005-be24-0ffb879b1130"
        )

        # CommunicationUserIdentifiers are not equal.
        assert CommunicationUserIdentifier(
            id="8:acs:6666e-9f06-482a-b5d8-20e3f26ef0cd_45ab2481-1c1c-4005-be24-0ffb879b1130"
        ) != CommunicationUserIdentifier(
            id="8:acs:555e-9f06-482a-b5d8-20e3f26ef0cd_45ab2481-1c1c-4005-be24-0ffb879b1130"
        )

        # MicrosoftTeamsUserIdentifiers are equal.
        assert MicrosoftTeamsUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130"
        ) == MicrosoftTeamsUserIdentifier(user_id="45ab2481-1c1c-4005-be24-0ffb879b1130")
        assert MicrosoftTeamsUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="PUBLIC"
        ) == MicrosoftTeamsUserIdentifier(user_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="PUBLIC")
        assert MicrosoftTeamsUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="DOD"
        ) == MicrosoftTeamsUserIdentifier(user_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="DOD")
        assert MicrosoftTeamsUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="GCCH"
        ) == MicrosoftTeamsUserIdentifier(user_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="GCCH")
        assert MicrosoftTeamsUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
            cloud="GCCH",
            is_anonymous=False,
        ) == MicrosoftTeamsUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
            cloud="GCCH",
            is_anonymous=False,
        )
        assert MicrosoftTeamsUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
            cloud="GCCH",
            is_anonymous=True,
        ) == MicrosoftTeamsUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
            cloud="GCCH",
            is_anonymous=True,
        )

        # MicrosoftTeamsUserIdentifiers are not equal.
        assert MicrosoftTeamsUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130"
        ) != MicrosoftTeamsUserIdentifier(user_id="55ab2481-1c1c-4005-be24-0ffb879b1130")
        assert MicrosoftTeamsUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="GCCH"
        ) != MicrosoftTeamsUserIdentifier(user_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="DOD")
        assert MicrosoftTeamsUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
            cloud="GCCH",
            is_anonymous=False,
        ) != MicrosoftTeamsUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
            cloud="GCCH",
            is_anonymous=True,
        )

        # MicrosoftTeamsAppIdentifiers are equal.
        assert MicrosoftTeamsAppIdentifier(
            app_id="45ab2481-1c1c-4005-be24-0ffb879b1130"
        ) == MicrosoftTeamsAppIdentifier(app_id="45ab2481-1c1c-4005-be24-0ffb879b1130")
        assert MicrosoftTeamsAppIdentifier(
            app_id="45ab2481-1c1c-4005-be24-0ffb879b1130"
        ) == MicrosoftTeamsAppIdentifier(app_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="PUBLIC")
        assert MicrosoftTeamsAppIdentifier(
            app_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="PUBLIC"
        ) == MicrosoftTeamsAppIdentifier(app_id="45ab2481-1c1c-4005-be24-0ffb879b1130")
        assert MicrosoftTeamsAppIdentifier(
            app_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="PUBLIC"
        ) == MicrosoftTeamsAppIdentifier(app_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="PUBLIC")
        assert MicrosoftTeamsAppIdentifier(
            app_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="DOD"
        ) == MicrosoftTeamsAppIdentifier(app_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="DOD")
        assert MicrosoftTeamsAppIdentifier(
            app_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="GCCH"
        ) == MicrosoftTeamsAppIdentifier(app_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="GCCH")

        # MicrosoftTeamsAppIdentifiers are not equal.
        assert MicrosoftTeamsAppIdentifier(
            app_id="54ab2481-1c1c-4005-be24-0ffb879b1130"
        ) != MicrosoftTeamsAppIdentifier(app_id="45ab2481-1c1c-4005-be24-0ffb879b1130")
        assert MicrosoftTeamsAppIdentifier(
            app_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="PUBLIC"
        ) != MicrosoftTeamsAppIdentifier(app_id="45ab2481-1c1c-4005-be24-0ffb879b1130", cloud="DOD")

        # PhoneNumberIdentifiers are equal.
        assert PhoneNumberIdentifier(value="+112345556789") == PhoneNumberIdentifier(value="+112345556789")

        # PhoneNumberIdentifiers are not equal.
        assert PhoneNumberIdentifier(value="+112345556789") != PhoneNumberIdentifier(value="+512345556789")

        # TeamsExtensionUserIdentifiers are equal.
        assert TeamsExtensionUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
            tenant_id="tenant123",
            resource_id="resource123",
            cloud="PUBLIC"
        ) == TeamsExtensionUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
            tenant_id="tenant123",
            resource_id="resource123",
            cloud="PUBLIC"
        )

        assert TeamsExtensionUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
            tenant_id="tenant123",
            resource_id="resource123",
            cloud="DOD"
        ) == TeamsExtensionUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
            tenant_id="tenant123",
            resource_id="resource123",
            cloud="DOD"
        )

        assert TeamsExtensionUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
            tenant_id="tenant123",
            resource_id="resource123",
            cloud="GCCH"
        ) == TeamsExtensionUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
            tenant_id="tenant123",
            resource_id="resource123",
            cloud="GCCH"
        )

        # TeamsExtensionUserIdentifiers are not equal.
        assert TeamsExtensionUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
            tenant_id="tenant123",
            resource_id="resource123",
            cloud="PUBLIC"
        ) != TeamsExtensionUserIdentifier(
            user_id="55ab2481-1c1c-4005-be24-0ffb879b1130",
            tenant_id="tenant123",
            resource_id="resource123",
            cloud="PUBLIC"
        )

        assert TeamsExtensionUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
            tenant_id="tenant123",
            resource_id="resource123",
            cloud="PUBLIC"
        ) != TeamsExtensionUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
            tenant_id="tenant456",
            resource_id="resource123",
            cloud="PUBLIC"
        )

        assert TeamsExtensionUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
            tenant_id="tenant123",
            resource_id="resource123",
            cloud="PUBLIC"
        ) != TeamsExtensionUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
            tenant_id="tenant123",
            resource_id="resource456",
            cloud="PUBLIC"
        )

        assert TeamsExtensionUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
            tenant_id="tenant123",
            resource_id="resource123",
            cloud="PUBLIC"
        ) != TeamsExtensionUserIdentifier(
            user_id="45ab2481-1c1c-4005-be24-0ffb879b1130",
            tenant_id="tenant123",
            resource_id="resource123",
            cloud="DOD"
        )
        
        # UnknownIdentifiers are equal.
        assert UnknownIdentifier(identifier="28:ag08-global:01234567-89ab-cdef-0123-456789abcdef") == UnknownIdentifier(
            identifier="28:ag08-global:01234567-89ab-cdef-0123-456789abcdef"
        )

        # UnknownIdentifiers are not equal.
        assert UnknownIdentifier(identifier="48:8888-global:01234567-89ab-cdef-0123-456789abcdef") != UnknownIdentifier(
            identifier="48:ag08-global:01234567-89ab-cdef-0123-456789abcdef"
        )


def _assert_raw_id(identifier, want):
    # type: (CommunicationIdentifier, str) -> None
    assert identifier.raw_id == want


def _assert_communication_identifier(raw_id, want):
    # type: (str, CommunicationIdentifier) -> None
    got = identifier_from_raw_id(raw_id)
    assert got.raw_id == want.raw_id
    assert got.kind == want.kind
    assert len(got.properties) == len(want.properties)
    for key in want.properties:
        assert key in got.properties
        assert got.properties[key] == want.properties[key]

def _assert_phonenumber_identifier(raw_id, want, withIsAnonymous=False, withAssertedId=False):
    # type: (str, PhoneNumberIdentifier, Optional[dict]) -> None
    got = identifier_from_raw_id(raw_id)
    assert got.raw_id == want.raw_id
    assert got.kind == want.kind
    for key in want.properties:
        assert key in got.properties
        assert got.properties[key] == want.properties[key]
    if withIsAnonymous:
        # Check if both want and got have 'is_anonymous' and 'asserted_id'properties
        assert "is_anonymous" in want.properties
        assert "is_anonymous" in got.properties
        assert got.properties["is_anonymous"] == want.properties["is_anonymous"]
    if withAssertedId:
        assert "asserted_id" in want.properties
        assert "asserted_id" in got.properties
        assert got.properties["asserted_id"] == want.properties["asserted_id"]


def _assert_roundtrip(raw_id):
    # type: (str) -> None
    assert identifier_from_raw_id(raw_id).raw_id == raw_id
