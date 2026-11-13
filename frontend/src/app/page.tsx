import StatsCard from "@/components/dashboard/stats-card";
import { getTenders } from "@/lib/api";
import TenderTable from "@/components/tenders/tender-table";
import PageHeading from "@/components/dashboard/page-heading";

export default async function DashboardPage() {
  const tenders = await getTenders();

  const total = tenders.length;

  const inReview = tenders.filter(
    (tender) => tender.status === "in_review"
  ).length;

  const submitted = tenders.filter(
    (tender) => tender.status === "submitted"
  ).length;

  const won = tenders.filter(
    (tender) => tender.status === "won"
  ).length;

  return (
    <div className="space-y-6">
      <PageHeading/>

      <section aria-label="Dashboard statistics">
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-4">
        <StatsCard title="Total tenders" value={total}/>
        <StatsCard title="In review" value={inReview}/>
        <StatsCard title="Submitted" value={submitted}/>
        <StatsCard title="Won" value={won}/>
      </div>
      </section>
      
      <TenderTable tenders={tenders}/>
    </div>
  )
}