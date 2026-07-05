"""Custom types for ha-clickup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import ClickUpApiClient
    from .coordinator import BlueprintDataUpdateCoordinator


type ClickUpConfigEntry = ConfigEntry[ClickUpData]


@dataclass
class ClickUpData:
    """Data for the Blueprint integration."""

    client: ClickUpApiClient
    coordinator: BlueprintDataUpdateCoordinator
    integration: Integration
