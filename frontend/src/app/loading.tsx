export default function Loading() {
  return (
    <div role="status" aria-label="Loading tenders" className="space-y-6">
      <span className="sr-only">Loading tenders...</span>

      <div aria-hidden="true" className="space-y-6 motion-safe:animate-pulse">
        <div className="space-y-2">
          <div className="h-8 w-40 rounded bg-slate-200" />
          <div className="h-4 w-64 max-w-full rounded bg-slate-200" />
        </div>

        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-4">
          {Array.from({ length: 4 }, (_, index) => (
            <div
              key={index}
              className="rounded-xl border border-slate-200 bg-white p-5"
            >
              <div className="h-4 w-24 rounded bg-slate-200" />
              <div className="mt-3 h-8 w-16 rounded bg-slate-200" />
            </div>
          ))}
        </div>

        <div className="rounded-xl border border-slate-200 bg-white p-5">
          <div className="mb-6 h-6 w-28 rounded bg-slate-200" />

          <div className="space-y-4">
            {Array.from({ length: 5 }, (_, index) => (
              <div
                key={index}
                className="h-10 w-full rounded bg-slate-100"
              />
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}