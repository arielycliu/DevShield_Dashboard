import * as React from 'react';
import { BarChart } from '@mui/x-charts/BarChart';

const uData = [5.6, 8.4, 7, 5.6, 9.8];
const pData = [4, 6, 5, 4, 7];
const xLabels = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
];

export default function ProductiveHoursBarGraph() {
    return (
        <div className='flex-center'>
            <h3>Productive hours w/ and w/o Devshield</h3>
            <BarChart
                width={500}
                height={300}
                series={[
                    { data: pData, label: 'Productive hours', id: 'pvId' },
                    { data: uData, label: 'Productive hours with Devshield', id: 'uvId' },
                ]}
                xAxis={[{ data: xLabels, scaleType: 'band' }]}
            />
        </div>
    );
}
