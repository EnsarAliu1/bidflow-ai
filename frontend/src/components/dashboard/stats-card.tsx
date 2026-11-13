import React from "react";

interface StatsCardProps {
    title: string;
    value: number;
    icon?: React.ReactNode;
}

export default function StatsCard({title, value, icon}: StatsCardProps) {
    return (
        <div className="p-5 bg-white border rounded-xl shadow-sm flex items-center justify-between">
            <div>
                <p className="text-sm font-medium text-gray-500">{title}</p>
                <p className="text-2xl font-bold mt-1">{value}</p>
            </div>

            {
                icon && (
                    <div className="p-3 bg-blue-50 text-blue-600 rounded-lg">
                        {icon}
                    </div>
                )
            }
        </div>
    )
}