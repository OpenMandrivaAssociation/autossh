%define name	autossh
%define version 1.4a
%define release %mkrel 1

Summary:	Automatically restart SSH sessions and tunnels
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	BSD
Group:		Networking/Other
URL:		http://www.harding.motd.ca/autossh/
Source:		%{name}-%{version}.tar.bz2
BuildRequires:	openssh-clients
Requires:	openssh
BuildRoot:	%{_tmppath}/%{name}-root

%description 
autossh is a program to start a copy of ssh and monitor it,
restarting it as necessary should it die or stop passing
traffic. The idea and the mechanism are from rstunnel
(Reliable SSH Tunnel), but implemented in C. 

%prep

%setup -q
%build
chmod 644 autossh.host rscreen
%configure
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -m755 autossh %{buildroot}%{_bindir}/
install -m644 autossh.1 %{buildroot}%{_mandir}/man1/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc CHANGES README autossh.host rscreen
%{_bindir}/autossh
%{_mandir}/man1/autossh.1*


