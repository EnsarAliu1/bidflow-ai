from enum import Enum


class TenderStatus(str, Enum):
    DRAFT = "draft"
    IN_REVIEW = "in_review"
    READY = "ready"
    SUBMITTED = "submitted"
    WON = "won"
    LOST = "lost"


ALLOWED_TRANSACTIONS: dict[
    TenderStatus, set[TenderStatus]
] = {
    TenderStatus.DRAFT: {
        TenderStatus.IN_REVIEW,
    },

    TenderStatus.IN_REVIEW: {
        TenderStatus.DRAFT,
        TenderStatus.READY,
    },

    TenderStatus.READY: {
        TenderStatus.IN_REVIEW,
        TenderStatus.SUBMITTED,
    },

    TenderStatus.SUBMITTED: {
        TenderStatus.WON,
        TenderStatus.LOST
    }
}


def can_transaction(
        current: TenderStatus,
        target: TenderStatus
) -> bool:
    return target in ALLOWED_TRANSACTIONS.get(current, set())
