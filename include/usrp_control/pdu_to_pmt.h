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


#ifndef INCLUDED_USRP_CONTROL_PDU_TO_PMT_H
#define INCLUDED_USRP_CONTROL_PDU_TO_PMT_H

#include <usrp_control/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace usrp_control {

    /*!
     * \brief <+description of block+>
     * \ingroup usrp_control
     *
     */
    class USRP_CONTROL_API pdu_to_pmt : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<pdu_to_pmt> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of usrp_control::pdu_to_pmt.
       *
       * To avoid accidental use of raw pointers, usrp_control::pdu_to_pmt's
       * constructor is in a private implementation
       * class. usrp_control::pdu_to_pmt::make is the public interface for
       * creating new instances.
       */
      static sptr make();
    };

  } // namespace usrp_control
} // namespace gr

#endif /* INCLUDED_USRP_CONTROL_PDU_TO_PMT_H */

