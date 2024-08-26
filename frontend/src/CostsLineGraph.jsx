import * as React from 'react';
import { LineChart } from '@mui/x-charts/LineChart';

const uData = [5800, 6300, 6800, 5900, 4700];
const pData = [2320, 2520, 2720, 2360, 1880];
const xLabels = [
  'Monday',
  'Tuesday',
  'Wednesday',
  'Thursday',
  'Friday',
];

export default function SimpleLineChart() {
  return (
    <div className='flex-center'>
        <h3>Cost of Developer Time: Pre- vs. Post-DevShield</h3>
        <LineChart
          width={500}
          height={300}
          series={[
            { data: pData, label: 'Current Dev Time Sinks' },
            { data: uData, label: 'Cost after Devshield' },
          ]}
          xAxis={[{ scaleType: 'point', data: xLabels }]}
        />
    </div>
  );
}
