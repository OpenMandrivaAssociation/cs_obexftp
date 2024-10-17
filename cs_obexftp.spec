%define name cs_obexftp
%define version 1.0.0.18
%define release 3

Summary: ObexFtp files transfert between two devices
Name: %{name}
Version: %{version}
Release: %{release}
License: GPLv2+
Group: Communications
URL: https://cs-obexftp.wiki.sourceforge.net/
Source0: http://kent.dl.sourceforge.net/sourceforge/cs-obexftp/%name-%version.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel >= 2.0
BuildRequires: obexftp-devel
Requires: obexftp
BuildArch: noarch

%description
Using the new CSharp Dll from swig portability of Openobex/ObexFtp to write
a nice GUI able to transfer file between two devices.

%prep
%setup -q -n %name-%version

%build
./configure --prefix=%_prefix --bindir=%_bindir --datadir=%_datadir --libdir=%_prefix/lib
%make

%install
rm -fr %buildroot
%makeinstall_std

%clean
rm -fr %buildroot

%files
%defattr(-,root,root)
%doc Cs-ObexFtp/ChangeLog THANKS todos
%_bindir/*
%_prefix/lib/csobexftp
%_prefix/lib/pkgconfig/*.pc


%changelog
* Mon Oct 13 2008 Funda Wang <fundawang@mandriva.org> 1.0.0.18-2mdv2009.1
+ Revision: 293255
- add versioned BR for mono (resgen2)
- add docs
- clearify license
- New version 1.0.0.18
- New version 1.0.0.14
- small adjustments
- renew tarball
- icomply to mandriva style
- import cs_obexftp


* Tue Oct 8 2007 Petit Eric <surfzoid@gmail.com> 0.1-1misc
- Made the rpm for Linux MDV2008

