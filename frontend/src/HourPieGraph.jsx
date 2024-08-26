import * as React from 'react';

import { PieChart, pieArcLabelClasses } from '@mui/x-charts/PieChart';

const data = [
    { label: '1on1s', value: 3, color: '#0088FE' },
    { label: 'Standups', value: 2, color: '#00C49F' },
    { label: 'Backlog / retrospectives', value: 2, color: '#FFBB28' },
    { label: 'Client facing', value: 5, color: '#FF8042' },
    { label: 'Design', value: 2, color: '#FF5242' },
    { label: 'Other internal tasks', value: 5, color: '#314ff7' },
];

const sizing = {
    margin: { right: 5 },
    width: 300,
    height: 300,
    legend: { hidden: false },
};
const TOTAL = data.map((item) => item.value).reduce((a, b) => a + b, 0);

const getArcLabel = (params) => {
    const percent = params.value / TOTAL;
    return `${(percent * 100).toFixed(0)}%`;
};

export default function HourPieGraph() {
    return (
        <div className='flex-center'>
            <h3>Average hour allocation across engineering org</h3>
            <PieChart
                series={[
                    {
                        data,
                        arcLabel: getArcLabel,
                    },
                ]}
                sx={{
                    [`& .${pieArcLabelClasses.root}`]: {
                        fill: 'white',
                        fontSize: 14,
                    },
                }}
                width={550}
                height={200}
            />
        </div>
    );
}
