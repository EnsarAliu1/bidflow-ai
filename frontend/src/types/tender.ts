export type TenderStatus =
    | "draft"
    | "in_review"
    | "ready"
    | "submitted"
    | "won"
    | "lost";

export interface Tender {
    id: string;
    title: string;
    organization: string;
    deadline: string;
    estimated_budget: number | null;
    status: TenderStatus
}