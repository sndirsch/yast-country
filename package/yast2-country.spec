#
# spec file for package yast2-country
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           yast2-country
Version:        4.2.1
Release:        0
Summary:        YaST2 - Country Settings (Language, Keyboard, and Timezone)
License:        GPL-2.0-only
Group:          System/YaST
Url:            https://github.com/yast/yast-country

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  perl-XML-Writer
BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  yast2-perl-bindings
BuildRequires:  yast2-testsuite
# For tests
BuildRequires:  rubygem(%rb_default_ruby_abi:rspec)
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)
# Fix to bnc#891053 (proper reading of ".target.yast2" on chroots)
BuildRequires:  yast2-core >= 3.1.12
# RSpec extensions for YaST
BuildRequires:  yast2-ruby-bindings >= 3.1.26
# OSRelease.id
BuildRequires:  yast2 >= 3.2.9

Requires:       timezone
Requires:       yast2-perl-bindings
Requires:       yast2-trans-stats
# OSRelease.id
Requires:       yast2 >= 3.2.9
# Pkg::SetPackageLocale, Pkg::GetTextLocale
Requires:       yast2-pkg-bindings >= 2.15.3
# IconPath support for MultiSelectionBox
Requires:       yast2-core >= 2.16.28
Requires:       yast2-packager >= 2.23.3
# VMware detection (.probe.is_vmware)
Requires:       yast2-hardware-detection >= 3.1.6
Requires:       yast2-country-data
Requires:       yast2-ruby-bindings >= 1.0.0
Requires:       rubygem(%{rb_default_ruby_abi}:ruby-dbus)

# new API of ntp-client_proposal.rb
Conflicts:      yast2-ntp-client < 4.1.5

%description
Country specific data and configuration modules (language, keyboard,
timezone) for yast2.

%package data
Requires:       yast2-ruby-bindings >= 1.0.0

Summary:        YaST2 - Data files for Country settings
Group:          System/YaST

%description data
Data files for yast2-country together with the most often used API
functions (Language module)

%prep
%setup -q

%build
%yast_build

%install
%yast_install

%ifarch s390 s390x
rm -f %{buildroot}%{yast_desktopdir}/org.opensuse.yast.Keyboard.desktop
%endif

%yast_metainfo

# Policies
mkdir -p %{buildroot}%{_datadir}/polkit-1/actions

# common
%files
%doc %{yast_docdir}
%license COPYING
%{yast_moduledir}/Console.rb
%{yast_moduledir}/Keyboard.rb
%{yast_moduledir}/Timezone.rb
%dir %{yast_moduledir}/YaPI
%{yast_moduledir}/YaPI/TIME.pm
%{yast_moduledir}/YaPI/LANGUAGE.pm
%{yast_clientdir}/*.rb
%dir %{yast_libdir}/y2country
%{yast_libdir}/y2country/widgets
%{yast_ydatadir}/*.ycp
%{yast_ydatadir}/*.json
%{yast_yncludedir}
%{yast_scrconfdir}
%{yast_schemadir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_icondir}

%files data
%dir %{yast_ydatadir}/languages
%{yast_ydatadir}/languages/*.ycp
%{yast_moduledir}/Language.rb
%dir %{yast_libdir}/y2country
%{yast_libdir}/y2country/language_dbus.rb

%changelog
