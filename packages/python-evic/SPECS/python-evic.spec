%{?python_enable_dependency_generator}
%global pypi_name evic

# No tagged releases.  :/
%global commit 176cf0b076db331cf79dcab4232abd1158b183fa
%{?commit:%global shortcommit %(c="%{commit}"; /bin/echo ${c:0:7})}
%{?commit:%global git_date 20161101}
%{?commit:%global git_rel .git%{git_date}.%{shortcommit}}
%{?commit:%global git_ver -git%{git_date}-%{shortcommit}}


Name:		python-%{pypi_name}
Version:	0.1
Release:	0.21%{?git_rel}%{?dist}
Summary:	USB programmer for devices based on the Joyetech Evic VTC Mini

License:	GPLv3+
URL:		https://github.com/Ban3/python-%{pypi_name}
Source0:	%{url}/archive/%{commit}.tar.gz#/%{name}-%{version}%{?git_ver}.tar.gz

# Patches from upstream.
Patch0:		%{url}/pull/38.patch#/%{name}-0.1-all_PRs.patch

BuildArch:	noarch

BuildRequires:	help2man
BuildRequires:	systemd

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary:	%{summary}

BuildRequires:	python3-binstruct
BuildRequires:	python3-bitarray
BuildRequires:	python3-bitstruct
BuildRequires:	python3-click
BuildRequires:	python3-devel
BuildRequires:	python3-hidapi
BuildRequires:	python3-pillow
BuildRequires:	python3-setuptools
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-runner

Recommends:	python3-hidapi >= 0.7.99

%{?systemd_requires}

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{summary}.


%prep
%if "0%{?commit}" == "0"
%autosetup -p 1
%else  # "0#{?commit}" == "0"
%autosetup -p 1 -n %{name}-%{commit}
%endif # "0#{?commit}" == "0"


%build
%py3_build


%install
%py3_install

# Needed for help2man.
PYTHONPATH="%{buildroot}/%{python3_sitelib}:${PYTHONPATH}"
export PYTHONPATH="${PYTHONPATH%%':'}"

# Generate man-pages.
%{__mkdir} -p %{buildroot}%{_mandir}/man1				\
	%{buildroot}%{_udevrulesdir} %{buildroot}%{_unitdir}

for f in %{buildroot}%{_bindir}/* ; do
	file="$(%{_bindir}/basename ${f})"
	%{_bindir}/help2man	    	        \
		-o "%{buildroot}%{_mandir}/man1/${file}.1" -s 1 -N	\
		--version-string="%{version}" --no-discard-stderr ${f}
done

# Install udev-rules.
%{__mv} %{buildroot}%{_usr}/udev/* %{buildroot}%{_udevrulesdir}
%{__rm} -fr %{buildroot}%{_usr}/udev

# Install systemd unit.
%{__install} -pm0644 scripts/*.service %{buildroot}%{_unitdir}

# Remove clutter from man-page generation.
%{__rm} -fv %{buildroot}%{python3_sitelib}/%{pypi_name}/*.py{c,o}
%{_bindir}/find %{buildroot}%{python3_sitelib}/%{pypi_name}		\
	-name '__pycache__' -print0 | %{_bindir}/xargs -0 %{__rm} -rfv


%check
%{__python3} setup.py test


%post -n python3-%{pypi_name}
%systemd_post evic-usb-rtc-sync.service


%preun -n python3-%{pypi_name}
%systemd_preun evic-usb-rtc-sync.service


%postun -n python3-%{pypi_name}
%systemd_postun_with_restart evic-usb-rtc-sync.service


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/*
%{_mandir}/man1/*.1*
%{_udevrulesdir}/*.rules
%{_unitdir}/*.service
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.21.git20161101.176cf0b
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.20.git20161101.176cf0b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.19.git20161101.176cf0b
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.18.git20161101.176cf0b
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.17.git20161101.176cf0b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.16.git20161101.176cf0b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1-0.15.git20161101.176cf0b
- Enable python dependency generator

* Mon Jan 07 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.14.git20161101.176cf0b
- Subpackage python2-evic has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1-0.13.git20161101.176cf0b
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.12.git20161101.176cf0b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.11.git20161101.176cf0b
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1-0.10.git20161101.176cf0b
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.9.git20161101.176cf0b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Björn Esser <besser82@fedoraproject.org> - 0.1-0.8.git20161101.176cf0b
- Updated snapshot

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.7.git20160814.f916017
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.6.git20160814.f916017
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.5.git20160814.f916017
- Rebuild for Python 3.6

* Mon Oct 24 2016 Björn Esser <fedora@besser82.io> - 0.1-0.4.git20160814.f916017
- %%{_udevrulesdir} is not defined during srpm-build
- Fix invocation of %%autosetup

* Mon Oct 24 2016 Björn Esser <fedora@besser82.io> - 0.1-0.3.git20160814.f916017
- Initial import (rhbz 1387834)

* Mon Oct 24 2016 Björn Esser <fedora@besser82.io> - 0.1-0.2.git20160814.f916017
- Changes suggested during review (rhbz 1387834)
- Add BuildRequires: systemd
- Use %%{_udevrulesdir}
- Don't mark udev-rules as %%config(noreplace)

* Fri Oct 21 2016 Björn Esser <fedora@besser82.io> - 0.1-0.1.git20160814.f916017
- Initial package (rhbz 1387834)
