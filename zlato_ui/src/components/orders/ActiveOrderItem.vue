<template>
    <div>
        <v-card flat class="text-center ma-3">
            <v-layout row wrap>
                <v-flex md1>
                    {{active_order.instrument.name}}
                </v-flex>
                <v-flex md10>
                </v-flex>
                <v-flex md1>
                    {{active_order.price}}
                </v-flex>
                <v-flex md1>
                    {{active_order.title}}
                </v-flex>
                <v-flex md9>
                </v-flex>
                <v-flex md1>
                    <v-btn disabled=true>
                        Buy
                    </v-btn>
                </v-flex>
                <v-flex md1>
                    <v-btn>
                        Cancel
                    </v-btn>
                </v-flex>
            </v-layout>
        </v-card>
    </div>
</template>

<script>
export default {
    name: "ActiveOrderItem",
    props: ["active_order"],
    data() {
        return {
            instruments: '',
            instrument_name: ''
        }
    },
    methods: {

    },
    created() {
        
    }
};
</script>