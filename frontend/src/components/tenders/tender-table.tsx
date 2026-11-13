import type { Tender } from "@/types/tender";
import { formatBudget, formatDate } from "@/lib/formatters";
import StatusBadge from "./status-badge";

interface TenderTableProps {
    tenders: Tender[];
}

export default function TenderTable({ tenders }: TenderTableProps) {
    return (
        <section className="rounded-xl border border-slate-200 bg-white">
            <h2 className="border-b border-slate-200 px-5 py-4 text-lg font-semibold">
                Tenders
            </h2>

            {tenders.length === 0 ? (
                <div className="px-5 py-12 text-center">
                    <p className="font-medium text-slate-900">
                        No tenders yet
                    </p>
                    <p className="mt-2 text-sm text-slate-500">
                        Tenders will appear here once they are created
                    </p>
                </div>
            ) : (
                    <div className="overflow-x-auto">
                        <table className="w-full text-left text-sm">
                            <thead className="bg-slate-50 text-slate-600">
                                <tr>
                                    <th scope="col" className="px-5 py-3">Title</th>
                                    <th scope="col" className="px-5 py-3">Organization</th>
                                    <th scope="col" className="px-5 py-3">Deadline</th>
                                    <th scope="col" className="px-5 py-3 text-right">Budget</th>
                                    <th scope="col" className="px-5 py-3">Status</th>
                                </tr>
                            </thead>

                            <tbody className="divide-y divide-slate-200">
                                {tenders.map((tender) => (
                                    <tr key={tender.id}>
                                        <td className="px-5 py-4 font-medium text-slate-900">
                                            {tender.title}
                                        </td>
                                        <td className="px-5 py-4 text-slate-600">
                                            {tender.organization}
                                        </td>
                                        <td className="whitespace-nowrap px-5 py-4 text-slate-600">
                                            {formatDate(tender.deadline)}
                                        </td>
                                        <td className="whitespace-nowrap px-5 py-4 text-right text-slate-600">
                                            {formatBudget(tender.estimated_budget)}
                                        </td>
                                        <td className="px-5 py-4 font-medium text-slate-900">
                                            <StatusBadge status={tender.status}/>
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
            )}
        </section>
    )
}