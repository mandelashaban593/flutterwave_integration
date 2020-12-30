function forPayment(paymentParams) {
  FlutterwaveCheckout({
    ...paymentParams,
    callback: function (data) {
      // not currently used
    },
    onclose: function () {
      window.location.href = paymentParams.redirect_url;
    },
  });
}
