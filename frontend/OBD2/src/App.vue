<style>
html {
    overflow: hidden !important;
    scrollbar-width: none;
    -ms-overflow-style: none;
}

html::-webkit-scrollbar {
    width: 0;
    height: 0;
}
</style>
<template >
    <v-container>
        <v-row no-gutters>
            <v-col md="4">
                <v-card-actions class="justify-center">
                    <v-progress-circular :size="200" :width="15" color="white" :model-value="carData.SPEED">
                        <h2>{{ carData.SPEED }} MPH </h2>
                    </v-progress-circular>
                </v-card-actions>
            </v-col>
            <v-col md="4">
                <v-card-actions class="justify-center">
                    <div v-if="(carData.RPM > 7000)">
                        <v-progress-circular :size="300" :width="15" color="red" :model-value="(carData.RPM/8000)">
                            <h2>
                                {{ carData.RPM }} RPM
                            </h2>
                        </v-progress-circular>
                    </div>
                    <div v-if="(carData.RPM > 5000)">
                        <v-progress-circular :size="300" :width="15" color="orange" :model-value="(carData.RPM/ 8000)">
                            <h2>
                                {{ carData.RPM }} RPM
                            </h2>
                        </v-progress-circular>
                    </div>
                    <div v-else>
                        <v-progress-circular :size="300" :width="15" color="yellow" :model-value="(carData.RPM/ 8000)">
                            <h2>
                                {{ carData.RPM }} RPM
                            </h2>
                        </v-progress-circular>
                    </div>




                </v-card-actions>
            </v-col>

            <v-col md="4">
                <v-card-actions class="justify-center">
                    <v-progress-circular :size="200" :width="15" color="blue" :model-value="carData.THROTTLE">
                        <h2>
                            Throttle: {{ carData.THROTTLE }}%
                        </h2>
                    </v-progress-circular>
                </v-card-actions>
            </v-col>
        </v-row>
        <v-row no-gutters>
            <v-col md="4">
                <v-card-actions class="justify-center">
                </v-card-actions>
            </v-col>
            <v-col md="4">
                <v-card-actions class="justify-center">
                </v-card-actions>
            </v-col>
            <v-col md="4">
                <v-card-actions class="justify-center">
                </v-card-actions>
            </v-col>
        </v-row>
        <v-row no-gutters>
            <v-col md="4">
                <v-card-actions class="justify-center">
                    <h2>
                        Intake: {{ carData.BOOST }} PSI
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
                        Oil Temp: {{ carData.TEMP }}°C
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
        timeout: 500
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
