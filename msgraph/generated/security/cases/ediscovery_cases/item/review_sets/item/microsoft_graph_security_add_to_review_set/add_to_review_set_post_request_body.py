from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.security.additional_data_options import AdditionalDataOptions
    from ........models.security.ediscovery_search import EdiscoverySearch

@dataclass
class AddToReviewSetPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The additionalDataOptions property
    additional_data_options: Optional[AdditionalDataOptions] = None
    # The search property
    search: Optional[EdiscoverySearch] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AddToReviewSetPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AddToReviewSetPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AddToReviewSetPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models.security.additional_data_options import AdditionalDataOptions
        from ........models.security.ediscovery_search import EdiscoverySearch

        from ........models.security.additional_data_options import AdditionalDataOptions
        from ........models.security.ediscovery_search import EdiscoverySearch

        fields: Dict[str, Callable[[Any], None]] = {
            "additionalDataOptions": lambda n : setattr(self, 'additional_data_options', n.get_enum_value(AdditionalDataOptions)),
            "search": lambda n : setattr(self, 'search', n.get_object_value(EdiscoverySearch)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("additionalDataOptions", self.additional_data_options)
        writer.write_object_value("search", self.search)
        writer.write_additional_data_value(self.additional_data)
    

