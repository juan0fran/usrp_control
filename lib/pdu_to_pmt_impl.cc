/* -*- c++ -*- */
/*
 * Copyright 2017 <+YOU OR YOUR COMPANY+>.
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "pdu_to_pmt_impl.h"

#include <string.h>
#include <cstdio>

namespace gr {
  namespace usrp_control {

    pdu_to_pmt::sptr
    pdu_to_pmt::make()
    {
      return gnuradio::get_initial_sptr
        (new pdu_to_pmt_impl());
    }

    /*
     * The private constructor
     */
    pdu_to_pmt_impl::pdu_to_pmt_impl()
      : gr::block("pdu_to_pmt",
              gr::io_signature::make(0,0,0),
              gr::io_signature::make(0,0,0))
    {
        message_port_register_out(pmt::mp("out"));
        message_port_register_in(pmt::mp("in"));
        set_msg_handler(pmt::mp("in"),
                        boost::bind(&pdu_to_pmt_impl::msg_handler, this, _1));
    }

    /*
     * Our virtual destructor.
     */
    pdu_to_pmt_impl::~pdu_to_pmt_impl()
    {
    }

    void
    pdu_to_pmt_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      /* <+forecast+> e.g. ninput_items_required[0] = noutput_items */
    }

    int
    pdu_to_pmt_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      return 0;
    }

    void
    pdu_to_pmt_impl::msg_handler(pmt::pmt_t pmt_msg)
    {
        pmt::pmt_t msg = pmt::cdr(pmt_msg);
        unsigned int msg_size = pmt::length(msg);
        uint8_t data_in[1024];
        char str[256];
        long freq;
        size_t offset(0);

        memcpy(data_in, pmt::uniform_vector_elements(msg, offset), msg_size);
        std::printf("Received: %s\n", data_in);
        sscanf((char *) data_in, "F%s", str);
        freq = atol(str);
        message_port_pub(pmt::mp("out"),
                pmt::cons(pmt::mp("freq"),
                            pmt::from_long(freq)));

    }

  } /* namespace usrp_control */
} /* namespace gr */
