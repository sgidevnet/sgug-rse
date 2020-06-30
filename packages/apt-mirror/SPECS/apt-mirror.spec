Name:            apt-mirror
Version:         0.4.5
Release:         5%{?dist}
Summary:         APT sources mirroring tool

Group:           Development/Tools
License:         GPLv2+
# proof of licensing: http://packages.debian.org/changelogs/pool/main/a/apt-mirror/apt-mirror_0.4.5-1/apt-mirror.copyright (GPLv2+)
URL:             http://apt-mirror.sourceforge.net/
Source0:         http://downloads.sourceforge.net/%{name}/%{name}_%{version}.orig.tar.gz
Source1:         Debian-mirror.list
Source2:         clean.sh
Patch0:          %{name}.patch
BuildArch:       noarch
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:        wget


%description
A small and efficient tool that lets you mirror a part of or
the whole Debian GNU/Linux distribution or any other apt sources.

Main features:
 * It uses a config similar to apts <sources.list>
 * It's fully pool comply
 * It supports multithreaded downloading
 * It supports multiple architectures at the same time
 * It can automatically remove unneeded files
 * It works well on overloaded channel to internet
 * It never produces an inconsistent mirror including while mirroring
 * It works on all POSIX complied systems with perl and wget

%prep
%setup -q
%patch0 -p1 -b .mirror


%build


%install
rm -rf %{buildroot}

mkdir -p \
      %{buildroot}/var/spool/%{name}/var

mkdir -p \
      %{buildroot}/var/spool/%{name}/skel

mkdir -p \
      %{buildroot}/var/spool/%{name}/mirror

install -Dpm 755 %{name} \
        %{buildroot}%{_sbindir}/%{name}

install -Dpm 644 %{SOURCE1} \
        %{buildroot}%{_sysconfdir}/%{name}.list

mkdir -p %{buildroot}%{_mandir}/man1/
      pod2man %{name} | gzip -9 -c > %{name}.1.gz
      install -p -m 0644 %{name}.1.gz \
      %{buildroot}%{_mandir}/man1/%{name}.1.gz

install -Dpm 755 %{SOURCE2} \
        %{buildroot}/var/spool/%{name}/var/clean.sh



%files
%defattr(-,root,root,-)
%doc CHANGELOG TODO
%{_sbindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%config (noreplace) %{_sysconfdir}/%{name}.list
/var/spool/%{name}/


%changelog
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep 28 2008 Simon Wesp <cassmodiah@fedoraproject.org> 0.4.5-3
- Correct License #464308 Comment 1 and add a comment below License-Tag

* Sun Sep 28 2008 Simon Wesp <cassmodiah@fedoraproject.org> 0.4.5-2
- Correct spec - Bug #464308 Comment 1
- Add Dummyfile to use clean.sh

* Sat Sep 27 2008 Simon Wesp <cassmodiah@fedoraproject.org> 0.4.5-1
- Initial Release
