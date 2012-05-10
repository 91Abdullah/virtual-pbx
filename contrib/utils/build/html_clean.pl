#!/usr/bin/perl
########################################################################
#
# $Id: html_clean.pl,v 1.19 2012-04-01 20:35:51 gosha Exp $
#
# Copyright (c) 2009 Okunev Igor <igor[at]prv.mts-nn.ru>
#
########################################################################
$^I = '.bak';

undef $/; $_ = <>;

if ( $ARGV =~ /statements\.tt$/ ) {
	# workaround - MIME::Lite->as_string deforms long strings...
	s#\n\s+#\n#gs;
} else {
	s#>\s+<#><#gs;
	s#\%\]\s+#%] #gs;
	s#\s+\[\%# [%#gs;
	s#>\s+#> #gs;
	s#\s+<# <#gs;
}

my $xvb_version = $ENV{'XVB_VERSION'} ;

if ( $xvb_version ) {
	$xvb_version =~ s#^1_##;
	my $date = gmtime;
	s#(</body>)?\s*</html>#<p align='center' class='copyright'><br><a href='/xvb/XVB.pdf?a=msg_download'>XVB - VirtualPBX</a> v.2, build: $xvb_version ( $date GMT ) / <a href='http://code.google.com/p/virtual-pbx/wiki/CommercialSupport'>Commercial Support</a><br><br><b>-- (c) 2009-2012 by <a href='http://home.sinn.ru/~gosha/'>Igor Okunev</a>. All rights reserved. --</b></p>$1</html>#;
}

print;
