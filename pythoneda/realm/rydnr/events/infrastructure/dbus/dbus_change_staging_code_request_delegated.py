# vim: set fileencoding=utf-8
"""
pythoneda/realm/rydnr/events/infrastructure/dbus/dbus_change_staging_code_request_delegated.py

This file declares DbusChangeStagingCodeRequestDelegated.

Copyright (C) 2023-today rydnr's pythoneda-realm-rydnr/events-infrastructure

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from dbus_next import Message
from dbus_next.service import signal
import json
from pythoneda.shared import Event
from pythoneda.shared.infrastructure.dbus import DbusEvent
from pythoneda.realm.rydnr.events import ChangeStagingCodeRequestDelegated
from pythoneda.shared import BaseObject
from pythoneda.shared.artifact_changes.events.infrastructure.dbus import DBUS_PATH
from typing import List, Type


class DbusChangeStagingCodeRequestDelegated(DbusEvent):
    """
    D-Bus interface for ChangeStagingCodeRequestDelegated

    Class name: DbusChangeStagingCodeRequestDelegated

    Responsibilities:
        - Define the d-bus interface for the ChangeStagingCodeRequestDelegated event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusChangeStagingCodeRequestDelegated.
        """
        super().__init__(
            "pythoneda_realm_rydnr_events_ChangeStagingCodeRequestDelegated"
        )

    @signal()
    def ChangeStagingCodeRequestDelegated(self, change: "s"):
        """
        Defines the ChangeStagingCodeRequestDelegated d-bus signal.
        :param change: The change.
        :type change: str
        """
        pass

    @classmethod
    def path(cls) -> str:
        """
        Retrieves the d-bus path.
        :return: Such value.
        :rtype: str
        """
        return DBUS_PATH

    @classmethod
    def transform(cls, event: ChangeStagingCodeRequestDelegated) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.realm.rydnr.events.ChangeStagingCodeRequestDelegated
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.message,
            event.repository_url,
            event.branch,
            event.repository_folder,
            json.dumps(event.previous_event_ids),
            event.id,
        ]

    @classmethod
    def sign(cls, event: ChangeStagingCodeRequestDelegated) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.realm.rydnr.events.ChangeStagingCodeRequestDelegated
        :return: The signature.
        :rtype: str
        """
        return "ssssss"

    @classmethod
    def parse(cls, message: Message) -> ChangeStagingCodeRequestDelegated:
        """
        Parses given d-bus message containing a ChangeStagingCodeRequestDelegated event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The ChangeStagingCodeRequestDelegated event.
        :rtype: pythoneda.realm.rydnr.events.ChangeStagingCodeRequestDelegated
        """
        (
            msg,
            repository_url,
            branch,
            repository_folder,
            prev_event_ids,
            event_id,
        ) = message.body
        return ChangeStagingCodeRequestDelegated(
            msg,
            repository_url,
            branch,
            repository_folder,
            json.loads(prev_event_ids),
            event_id,
        )

    @classmethod
    def event_class(cls) -> Type[Event]:
        """
        Retrieves the specific event class.
        :return: Such class.
        :rtype: type(pythoneda.shared.Event)
        """
        return ChangeStagingCodeRequestDelegated


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
