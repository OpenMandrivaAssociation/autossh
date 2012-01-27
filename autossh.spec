Summary:	Automatically restart SSH sessions and tunnels
Name:		autossh
Version:	1.4c
Release:	%mkrel 1
License:	BSD
Group:		Networking/Other
URL:		http://www.harding.motd.ca/autossh/
Source:		http://www.harding.motd.ca/autossh/%{name}-%{version}.tgz
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
%configure2_5x
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
