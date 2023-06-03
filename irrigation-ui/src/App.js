import React, {useEffect, useState} from "react";
import axios from "axios";
import {Switch} from "@mui/material";

const Relays = () => {
    const [relays, setRelays] = useState([]);
    const host = 'http://localhost:5000';

    const fetchRelays = async () => {
        const response = await axios.get(`${host}/controllers/schedules`);
        const data = response.data;
        data.relays.forEach(obj => obj.running = false);
        setRelays(data.relays);
    };

    const handleToggle = (relay) => {
        if (relays[relay - 1].running) {
            axios.delete(`${host}/zones/${relay}`);
        } else {
            axios.post(`${host}/zones/${relay}`);
        }
        const newRelays = relays.map((r) => {
            if (r.relay === relay) {
                r.running = !r.running;
            }
            return r;
        });
        setRelays(newRelays);
    };

    useEffect(() => {
        fetchRelays();
    }, []);

    return (
        <div>
            {relays.map((relay) => (
                <div key={relay.relay}>
                    <b>{relay.name}</b>
                    <Switch
                        variant="outlined"
                        checked={relay.running}
                        onChange={() => handleToggle(relay.relay)}
                    />
                </div>
            ))}
        </div>
    );
};

export default Relays;
