import type { Tender } from "@/types/tender";

export async function getTenders(): Promise<Tender[]> {
    const baseUrl = process.env.API_BASE_URL;

    if (!baseUrl) {
        throw new Error("API_BASE_URL is not configured")
    }

    const response = await fetch(`${baseUrl}/tenders`, {
        cache: "no-store",
    })

    if (!response.ok) {
        throw new Error(`The tender process failed: HTTP ${response.status}`);
    }

    const tenders: Tender[] = await response.json();

    return tenders;
}