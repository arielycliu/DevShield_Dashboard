import { useState } from 'react'
import './App.css'
import CostsLineGraph from './CostsLineGraph'
import CostsBarGraph from './CostsBarGraph'
import ProductiveHoursBarGraph from './ProductiveHoursBarGraph'
import HourPieGraph from './HourPieGraph'

function App() {

    return (
        <>
            <div className='flex'>
                <CostsLineGraph />
                <CostsBarGraph />
            </div>
            <div className='flex'>
                <ProductiveHoursBarGraph />
                <HourPieGraph />
            </div>
        </>
    )
}

export default App
