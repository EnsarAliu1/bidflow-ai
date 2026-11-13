"use client";

import { CircleAlert } from "lucide-react";
import { useRouter } from "next/navigation";
import { startTransition } from "react";

interface ErrorPageProps {
  error: Error & { digest?: string };
  reset: () => void;
}

export default function ErrorPage({ reset }: ErrorPageProps) {
    const router = useRouter();

function handleRetry() {
  startTransition(() => {
    router.refresh();
    reset();
  });
}

  return (
    <section
      role="alert"
      className="rounded-xl border border-slate-200 bg-white px-6 py-12 text-center"
    >
      <CircleAlert
        aria-hidden="true"
        className="mx-auto h-10 w-10 text-red-500"
      />

      <h1 className="mt-4 text-xl font-semibold text-slate-900">
        Unable to load tenders
      </h1>

      <p className="mt-2 text-sm text-slate-500">
        Check your connection and try again.
      </p>

      <button
        type="button"
        onClick={handleRetry}
        className="mt-6 rounded-lg bg-[#4F46E5] px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-indigo-700 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
      >
        Try again
      </button>
    </section>
  );
}