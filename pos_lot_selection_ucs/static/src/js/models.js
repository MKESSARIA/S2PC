odoo.define('pos_lot_selection_ucs.model', function(require){
    // var screens = require('point_of_sale.screens');
    var core = require('web.core');
    // var gui = require('point_of_sale.gui');
    var models = require('point_of_sale.models');
    // var PopupWidget = require('point_of_sale.popups');
    var QWeb = core.qweb;
    const Registries = require('point_of_sale.Registries');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const OrderWidget = require('point_of_sale.OrderWidget');


    models.Product = models.Product.extend({

        isAllowOnlyOneLot: function() {
            const productUnit = this.get_unit();
            return this.tracking === 'serial' || !productUnit || !productUnit.is_pos_groupable;
        },

    });

    models.Orderline = models.Orderline.extend({
        get_required_number_of_lots: function(){
            return Math.abs(this.quantity);
        },
    })



});
