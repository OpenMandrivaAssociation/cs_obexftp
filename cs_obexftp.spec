%define name cs_obexftp
%define version 1.0.0.18
%define release %mkrel 1

Summary: ObexFtp files transfert between two devices
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL+
Group: Communications
URL: http://cs-obexftp.wiki.sourceforge.net/
Source0: http://kent.dl.sourceforge.net/sourceforge/cs-obexftp/%name-%version.tar.bz2
BuildRequires: mono-devel
BuildRequires: obexftp-devel
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
%_bindir/*
%_prefix/lib/csobexftp
%_prefix/lib/pkgconfig/*.pc
