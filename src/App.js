import React from 'react';
import PropTypes from 'prop-types';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Slider from '@mui/material/Slider';
import Player from './Player';
import {maxPlayersCount} from './utils';

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
    const handleChange = (event, newValue) => {
        setValue(newValue);
    };
    const handleSliderPlayerChange = (event, val) => {
        setPlayerCount(val);
    };

    const valueSliderPlayer = (value) => {
        return `${value} Players`;
    };
    const marksPlayerSlider = [];
    const Players = [];
    const players = {};
    for (let i = 2; i <= maxPlayersCount; i++) {
        marksPlayerSlider.push({value: i, label: `${i}`});
    }
    for (let i = 1; i <= maxPlayersCount; i++) {
        players[i] = {cards: [{rank: 0, suit: 0}, {rank: 0, suit: 0}]};
    }
    for (let i = 1; i <= maxPlayersCount; i++) {
        const handlePlayerChange = (val) => {
            players[i] = val;
        }
        Players.push({
            onChange: handlePlayerChange,
            i
        });
    }
    return (
        <Box sx={{ width: '100%' }}>
            <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
                <Tabs value={value} onChange={handleChange} aria-label="navbar" centered>
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
                        max={maxPlayersCount}
                    />
                    You selected: {playerCount} players
                </Box>
                <Box sx={{width: '100%'}}>
                    <Grid container spacing={2}>
                        {Players.map((player, index) => {
                            if (index < playerCount) {
                                return (
                                    <Grid item xs={3}>
                                        <Player onChange={player.onChange} num={player.i}/>
                                    </Grid>
                                )
                            }
                            })
                        }
                    </Grid>
                </Box>
            </CustomTabPanel>
            <CustomTabPanel value={value} index={2}>

            </CustomTabPanel>
        </Box>
    );
};

export default App;
