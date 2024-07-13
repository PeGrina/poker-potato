import React from 'react';
import PropTypes from 'prop-types';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import Box from '@mui/material/Box';
import Slider from '@mui/material/Slider';
import Player from './Player';
import { ranks, suits, getCardInfo } from './utils';
import {Typography} from "@mui/material";
function CustomTabPanel(props) {
    const { children, value, index, ...other } = props;

    return (
        <div
            role="tabpanel"
            hidden={value !== index}
            id={`simple-tabpanel-${index}`}
            aria-labelledby={`simple-tab-${index}`}
            {...other}
        >
            {value === index && <Box sx={{ p: 3 }}>{children}</Box>}
        </div>
    );
}

CustomTabPanel.propTypes = {
    children: PropTypes.node,
    index: PropTypes.number.isRequired,
    value: PropTypes.number.isRequired,
};

function a11yProps(index) {
    return {
        id: `simple-tab-${index}`,
        'aria-controls': `simple-tabpanel-${index}`,
    };
}

const App = () => {
    const [value, setValue] = React.useState(0);
    const [playerCount, setPlayerCount] = React.useState(2);
    const [player, setPlayer] =
        React.useState({cards: [{rank: 0, suit: 0}, {rank: 0, suit: 0}]});

    const handleChange = (event, newValue) => {
        setValue(newValue);
    };
    const handleSliderPlayerChange = (event, val) => {
        setPlayerCount(val);
    };
    const handlePlayerChange = (val) => {
        console.log(val);
        setPlayer(val);
    }
    const valueSliderPlayer = (value) => {
        return `${value} Players`;
    };
    const marksPlayerSlider = [
        {
            value: 2,
            label: '2',
        },
        {
            value: 3,
            label: '3',
        },
        {
            value: 4,
            label: '4',
        },
        {
            value: 5,
            label: '5',
        },
        {
            value: 6,
            label: '6',
        },
        {
            value: 7,
            label: '7',
        },
        {
            value: 8,
            label: '8',
        }
    ];

    return (
        <Box sx={{ width: '100%' }}>
            <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
                <Tabs value={value} onChange={handleChange} aria-label="basic tabs example">
                    <Tab label="Главная" {...a11yProps(0)} />
                    <Tab label="Калькулятор" {...a11yProps(1)} />
                    <Tab label="О нас" {...a11yProps(2)} />
                </Tabs>
            </Box>
            <CustomTabPanel value={value} index={0}>
                Данный сайт - калькулятор для покера.
            </CustomTabPanel>
            <CustomTabPanel value={value} index={1}>
                <Box sx={{width: 300}}>
                    Select players count on the table
                    <Slider
                        aria-label="Players count"
                        defaultValue={2}
                        getAriaValueText={valueSliderPlayer}
                        valueLabelDisplay="auto"
                        shiftStep={1}
                        step={1}
                        onChange={handleSliderPlayerChange}
                        marks={marksPlayerSlider}
                        min={2}
                        max={8}
                    />
                    You selected: {playerCount} players
                </Box>
                <Box sx={{width: 300}}>
                    <Typography variant="div" color="textSecondary">Selected cards: {player.cards.map((card, i) => getCardInfo(card) + " ")}</Typography>
                    <Player onChange={handlePlayerChange}/>
                </Box>
            </CustomTabPanel>
            <CustomTabPanel value={value} index={2}>

            </CustomTabPanel>
        </Box>
    );
};

export default App;
