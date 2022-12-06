<template>
    <v-container>
        <v-row no-gutters>
            <v-col md="4">
                <v-card-actions class="justify-center">
                    <v-progress-circular :size="200" color="black" model-value="20"></v-progress-circular>
                </v-card-actions>
            </v-col>
            <v-col md="4">
                <v-card-actions class="justify-center">
                    <v-progress-circular :size="300" color="red" model-value="20"></v-progress-circular>
                </v-card-actions>
            </v-col>

            <v-col md="4">
                <v-card-actions class="justify-center">
                    <v-progress-circular :size="200" color="blue" model-value="20"></v-progress-circular>
                </v-card-actions>
            </v-col>
        </v-row>
        <v-row no-gutters>
            <v-col md="4">
                <v-card-actions class="justify-center">
                    <h3>
                        {{ carData.SPEED }}
                    </h3>
                </v-card-actions>
            </v-col>
            <v-col md="4">
                <v-card-actions class="justify-center">
                    <h3>
                        {{ carData.RPM }}
                    </h3>
                </v-card-actions>
            </v-col>
            <v-col md="4">
                <v-card-actions class="justify-center">
                    <h3>
                        {{ carData.THROTTLE }}
                    </h3>
                </v-card-actions>
            </v-col>
        </v-row>
        <v-row no-gutters>
            <v-col md="4">
                <v-card-actions class="justify-center">
                    <h2>
                        {{ carData.BOOST }}
                    </h2>
                </v-card-actions>
            </v-col>
            <v-col md="4">
                <v-card-actions class="justify-center">
                    <h1>
                    </h1>
                </v-card-actions>
            </v-col>
            <v-col md="4">
                <v-card-actions class="justify-center">
                    <h2>
                        {{ carData.TEMP }}
                    </h2>
                </v-card-actions>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import axios from "axios";

export default {
    name: 'App',
    components: {
    },

    data: () => ({
        carData: {},
        timeout: 1000
    }),
    mounted() {
        const timer = window.setTimeout(this.updatecarData, this.timeout);
    },
    methods: {
        updatecarData() {
            axios
                .get('http://127.0.0.1:5000')
                .then(response => {
                    this.carData = response.data
                })
                .catch(error => console.log(error))
        window.setTimeout(this.updatecarData, this.timeout);
        }
    }


}
</script>
