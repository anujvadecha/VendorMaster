<template>
  <div class="orders">
    <v-card>
      <v-card-title>Orders</v-card-title>
      <v-tabs vertical>
        <v-tab>
          <v-icon left>
            mdi-account
          </v-icon>
          Open
        </v-tab>
        <v-tab>
          <v-icon left>
            mdi-lock
          </v-icon>
          Executed
        </v-tab>
        <v-tab>
          <v-icon left>
            mdi-access-point
          </v-icon>
          Previous
        </v-tab>

        <v-tab-item>
          <v-card flat>
            <v-list three-line>
              <v-list-item-group v-model="model">
                <v-list-item>
                  <v-list-item-content>
                    <v-card class="d-flex flex-row pa-2" outlined tile>
                      <v-row ></v-row>
                      <v-row no-gutters align-self="middle">
                        <v-col cols="8">#TR1234567890</v-col>
                        <v-col cols="4"><v-chip>Limit</v-chip>50600</v-col>
                      </v-row>
                      <!--                        Arihant Gold 999-->
                      <!--                        <div>Delivery 3-10th Nov</div>-->
                      <!--                        <div>15:23:19</div>-->
                      <!--                        <v-chip>BUY</v-chip>-->
                      <!--                        200-->
                      <!--                        <v-btn>Cancel</v-btn>-->
                    </v-card>
                  </v-list-item-content>
                </v-list-item>
              </v-list-item-group>
            </v-list>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card flat>
            <v-card-text>
            </v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card flat>
            <v-card-text>
              <p>
                Fusce a quam. Phasellus nec sem in justo pellentesque facilisis. Nam eget dui. Proin viverra, ligula sit
                amet ultrices semper, ligula arcu tristique sapien, a accumsan nisi mauris ac eros. In dui magna,
                posuere eget, vestibulum et, tempor auctor, justo.
              </p>
            </v-card-text>
          </v-card>
        </v-tab-item>
      </v-tabs>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "Orders",
  data() {
    return {
      items: [
        {
          icon: 'mdi-inbox',
          text: 'Inbox',
        },
        {
          icon: 'mdi-star',
          text: 'Star',
        },
        {
          icon: 'mdi-send',
          text: 'Send',
        },
        {
          icon: 'mdi-email-open',
          text: 'Drafts',
        },
      ],
      model: 1,
    }
  }
};
</script>

<style scoped>
.orders {
  color: black;
}
</style>