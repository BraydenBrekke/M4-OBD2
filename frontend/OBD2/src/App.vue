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
                    Speed
                    </h3>
                </v-card-actions>
            </v-col>
            <v-col md="4">
                <v-card-actions class="justify-center">
                    <h3>
                    RPM
                    </h3>
                </v-card-actions>
            </v-col>
            <v-col md="4">
                <v-card-actions class="justify-center">
                    <h3>
                    Throttle
                    </h3>
                </v-card-actions>
            </v-col>
        </v-row>
        <v-row no-gutters>
            <v-col md="4">
                <v-card-actions class="justify-center">
                    <h2>
                        Boost
                    </h2>
                </v-card-actions>
            </v-col>
            <v-col md="4">
                <v-card-actions class="justify-center">
                    <h1>
                        Gear
                    </h1>
                </v-card-actions>
            </v-col>
            <v-col md="4">
                <v-card-actions class="justify-center">
                    <h2>
                        Gear
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
        //
    }),
    mounted() {
        axios.get("http://localhost:5000/")
      .then(response => {
         this.todosList = [...response.data].slice(0, 10)
      })
      .catch(err => {
         // Manage the state of the application if the request 
         // has failed      
      })
} 
}
</script>
