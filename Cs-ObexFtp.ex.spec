%define name cs_obexftp
%define version 1.0.0.13
%define release %mkrel 1

Summary: ObexFtp files transfert between two devices
Name: %{name}
Version: %{version}
Release: %{release}
License: GNU
Group: Communications
URL: http://cs-obexftp.wiki.sourceforge.net/
Packager: Petit Eric <surfzoid@gmail.com>
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 

#Enfin, il faut indiquer ou trouver les sources, grâce au tag Source. Le système prendra le fichier de ce nom dans le répertoire ~/rpm/SOURCES

Source: %{name}-%{version}.tar.bz2

BuildRequires: mono desktop-file-utils obexftp openobex 

%description
Using the new CSharp Dll from swig portability of Openobex/ObexFtp to write a nice GUI able to transfer file between two devices. More Info's here: http://cs-obexftp.wiki.sourceforge.net/'.

%prep
%setup -q -n %name-%version

%build
export LC_ALL=UTF-8
./configure --prefix=%_prefix --config=DEBUG_ANY_CPU
#./configure --prefix=/usr --config=DEBUG_ANY_CPU
make

%install
desktop-file-install --vendor=""                                 \
       --dir=%{buildroot}%{_datadir}/applications/   \
       %{buildroot}/%{_datadir}/applications/csobexftp.desktop
%makeinstall_std



%files
%defattr(755,root,users)
%_prefix/lib/cs_obexftp/
%_prefix/bin/cs-obexftp
%_prefix/share/icons/CsObexFtp.png
%_prefix/share/applications/csobexftp.desktop



