export default function Header() {
    return (
        <header className="flex items-center justify-between gap-4 border-b border-slate-200 bg-white px-6 py-4">
            <div className="min-w-0">
                <p className="truncate text-sm text-slate-500">
                    BidFlow Workspace
                </p>

                <p className="text-sm font-medium text-slate-700">
                    Dashboard
                </p>
            </div>

            <div
                role="img"
                aria-label="User's illustrative avatar"
                className="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-indigo-100 text-sm font-semibold text-indigo-700"
            >
                BF
            </div>
        </header>
    )
}