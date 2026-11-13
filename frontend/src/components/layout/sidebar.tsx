import Link from "next/link";
import {
  LayoutDashboard,
  BriefcaseBusiness,
  FileText,
  Bot,
  Zap,
  Settings,
} from "lucide-react";

const upcomingModules = [
  { label: "Tenders", icon: BriefcaseBusiness },
  { label: "Documents", icon: FileText },
  { label: "AI Assistant", icon: Bot },
  { label: "Automations", icon: Zap },
  { label: "Settings", icon: Settings },
];

export default function Sidebar() {
  return (
    <aside className="w-full shrink-0 bg-sidebar p-4 text-white md:min-h-screen md:w-60 md:p-5">
      <Link
        href="/"
        className="inline-block rounded text-xl font-bold focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-white"
      >
        BidFlow AI
      </Link>

      <nav
        aria-label="Main navigation"
        className="mt-4 flex gap-2 overflow-x-auto pb-2 md:mt-10 md:flex-col md:pb-0"
      >
        <Link
          href="/"
          aria-current="page"
          className="flex shrink-0 items-center gap-3 rounded-lg bg-primary px-3 py-2 text-sm font-medium focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white"
        >
          <LayoutDashboard aria-hidden="true" className="h-5 w-5" />
          Dashboard
        </Link>

        {upcomingModules.map(({ label, icon: Icon }) => (
          <button
            key={label}
            type="button"
            disabled
            className="flex shrink-0 cursor-not-allowed items-center gap-3 whitespace-nowrap rounded-lg px-3 py-2 text-left text-sm text-slate-400"
          >
            <Icon aria-hidden="true" className="h-5 w-5" />
            {label}
          </button>
        ))}
      </nav>
    </aside>
  );
}