<!-- views/product_template_views.xml -->
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="view_product_template_form_quotation" model="ir.ui.view">
        <field name="name">product.template.form.quotation</field>
        <field name="model">product.template</field>
        <field name="inherit_id" ref="product.product_template_only_form_view"/>
        <field name="arch" type="xml">
            <xpath expr="//header" position="inside">
                <button 
                    name="fetch_quotation" 
                    string="Actualizar Cotización" 
                    type="object" 
                    class="btn-primary"
                    invisible="not default_code"
                />
            </xpath>
            <xpath expr="//group[@name='group_general']" position="inside">
                <field name="quotation" widget="monetary" options="{'currency_field': 'currency_id'}"/>
                <field name="last_quotation_date" readonly="1"/>
            </xpath>
        </field>
    </record>
</odoo>