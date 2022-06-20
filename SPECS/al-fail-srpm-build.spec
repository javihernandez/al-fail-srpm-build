#
# spec file for package al-fail-srpm-build
#
# Copyright (c) 2022 CloudLinux Inc.
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


Name:           al-fail-srpm-build
Version:        0.0.1
Release:        1%{dist}
Summary:        RPM spec that won't create a SRPM

License:        GPL
Source0:        %{name}-%{version}.tar.gz

%description
This is a dummy spec file that will fail when trying to create a SRPM

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%post
%postun

%files
%license COPYING
%doc ChangeLog README

%changelog
* Mon Jun 20 2022 Javier Hernández
-
