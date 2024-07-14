import React from 'react';
import Card from '@mui/material/Card';
import PlayingCard from './PlayingCard';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import CardHeader from '@mui/material/CardActions';
import {getCardInfo} from "./utils";
import {Stack} from "@mui/material";

const Player = (props) => {
    const [card1, setCard1] = React.useState({rank: 0, suit: 0});
    const [card2, setCard2] = React.useState({rank: 0, suit: 0});
    const handleCard1Change = (val) => {
        setCard1(val);
        if (props.onChange !== null && props.onChange !== undefined) {
            props.onChange({cards: [val, card2]});
        }
    };
    const handleCard2Change = (val) => {
        setCard2(val);
        if (props.onChange !== null && props.onChange !== undefined) {
            props.onChange({cards: [card1, val]});
        }
    };
    return (<Card sx={{height:150, padding: 3}}>
        <CardHeader>
            <Stack spacing={2}>
                <Typography variant="h5" textAlign="center">Player {props.num}</Typography>
                <Typography variant="div" textAlign="center" color="textSecondary">Selected cards: {getCardInfo(card1)} {getCardInfo(card2)}</Typography>
            </Stack>
        </CardHeader>
        <Grid container spacing={2}>
            <Grid item xs={6}>
                <PlayingCard onChange={handleCard1Change} />
            </Grid>
            <Grid item xs={6}>
                <PlayingCard onChange={handleCard2Change} />
            </Grid>
        </Grid>
    </Card>);
}

export default Player;