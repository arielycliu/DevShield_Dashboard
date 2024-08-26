import * as React from 'react';
import { BarChart } from '@mui/x-charts/BarChart';

const uData = [5800, 6300, 6800, 5900, 4700];
const pData = [2320, 2520, 2720, 2360, 1880];
const xLabels = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
];

export default function CostsBarGraph() {
    return (
        <div className='flex-center'>
            <h3>Current Dev Time Sinks and Cost after Devshield</h3>
            <BarChart
                width={500}
                height={300}
                series={[
                    { data: pData, label: 'Current Dev Time Sinks', id: 'pvId', stack: 'total' },
                    { data: uData, label: 'Cost after Devshield', id: 'uvId', stack: 'total' },
                ]}
                xAxis={[{ data: xLabels, scaleType: 'band' }]}
            />
        </div>
    );
}
