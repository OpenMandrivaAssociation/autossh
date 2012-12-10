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


%changelog
* Fri Jan 27 2012 Andrey Bondrov <abondrov@mandriva.org> 1.4c-1mdv2011.0
+ Revision: 769401
- New version 1.4c, add Source url

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4b-4mdv2011.0
+ Revision: 610009
- rebuild

* Mon Feb 08 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.4b-3mdv2010.1
+ Revision: 502294
- use %%configure2_5x

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1.4b-2mdv2010.0
+ Revision: 436697
- rebuild

* Fri Jan 09 2009 Jérôme Soyer <saispo@mandriva.org> 1.4b-1mdv2009.1
+ Revision: 327420
- New version

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 1.4a-4mdv2009.0
+ Revision: 240435
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4a-2mdv2008.0
+ Revision: 83875
- rebuild


* Sun Dec 10 2006 Emmanuel Andry <eandry@mandriva.org> 1.4a-1mdv2007.0
+ Revision: 94424
- add buildrequires openssh-clients
- New version 1.4a
  drop patch
- Import autossh

* Sat May 06 2006 Nicolas L�cureuil <neoclust@mandriva.org> 1.3-1mdk
- New release 1.3
- use mkrel

* Sat Jun 04 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2f-2mdk
- rebuild

* Sun May 09 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.2f-1mdk
- 1.2f
- added P1 by Dmitry V. Levin <ldv@altlinux.org> (Fixed two uninitialized
  variable issues found by compiler.)

