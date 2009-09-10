%define name cs_obexftp
%define version 1.0.1.19
%define svnrel 293
%define release %mkrel -c r%{svnrel} 2

Summary: ObexFtp files transfert between two devices
Name: %{name}
Version: %{version}
Release: %{release}
License: GPLv2+
Group: Communications
URL: http://cs-obexftp.wiki.sourceforge.net/
Source0: http://kent.dl.sourceforge.net/sourceforge/cs-obexftp/%name-%version.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel >= 2.0
BuildRequires: obexftp-devel >= 0.2.3
Requires: obexftp >= 0.2.3
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
