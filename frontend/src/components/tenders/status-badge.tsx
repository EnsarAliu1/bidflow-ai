import { TenderStatus } from "@/types/tender";

interface StatusBadgeProps {
    status: TenderStatus;
}

const statusConfig: Record<
    TenderStatus,
    { label: string; className: string }
    > = {
    draft: {
            label: "Draft",
        className: "bg-slate-100 text-slate-700",
    },
        
    in_review: {
        label: "In review",
        className: "bg-blue-100 text-blue-700",
    },

    ready: {
        label: "Ready",
        className: "bg-purple-100 text-purple-700",
    },

    submitted: {
        label: "Submitted",
        className: "bg-teal-100 text-teal-700",
    },

    won: {
        label: "Won",
        className: "bg-green-100 text-green-700",
    },

    lost: {
        label: "Lost",
        className: "bg-red-100 text-red-700",
    }
}

export default function StatusBadge({ status }: StatusBadgeProps) {
    const config = statusConfig[status];

    return (
        <span
            className={`inline-flex rounded-full px-2.5 py-1 text-xs font-medium ${config.className}`}
        >
            {config.label}
        </span>
    );
}