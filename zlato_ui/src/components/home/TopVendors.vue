<template>
  <div>
    <v-card class="ma-2" flat outlined>
      <v-card-title>Our best rated vendors</v-card-title>
      <v-slide-group class="pa-1" show-arrows>
        <v-slide-item
          v-for="vendor in vendors"
          :key="vendor.vendor_id"
          v-slot=""
        >
          <v-card
            class="ma-3"
            height="180"
            width="140"
            @click="open_vendor_dialog(vendor.vendor_id)"
            v-bind:style="{
              'background-color': vendor.theme.css_header_background_color
            }"
            align="center"
          >
            <!--            <span-->

            <!--            >-->
            <!--              <v-row-->
            <!--                class=""-->
            <!--                style="height: 80%; width: 100%"-->
            <!--                align="center"-->
            <!--                            >-->
            <v-img max-width="80%" max-height="80%" :src="vendor.theme.logo" />
            <v-scale-transition> </v-scale-transition>
            <v-card-actions> {{ vendor.name }}</v-card-actions>
          </v-card>
        </v-slide-item>
      </v-slide-group></v-card
    >
  </div>
</template>

<script>
export default {
  name: "TopVendors",
  props: ["vendors"],
  methods: {
    open_vendor_dialog: function(vendor_id) {
      console.log(this.$store);
      console.log(vendor_id);
      var selected_vendor_item = this.$store.getters.get_vendor_instruments(
        vendor_id
      );
      this.$router.push({
        name: "Vendor",
        params: {
          vendor: selected_vendor_item.vendor.name,
          vendor_object: selected_vendor_item
        }
      });
    }
  }
};
</script>

<style scoped></style>
