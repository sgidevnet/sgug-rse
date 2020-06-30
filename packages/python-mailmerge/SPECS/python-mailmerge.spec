%global srcname mailmerge
%{?python_enable_dependency_generator}

Name:          python-%{srcname}
Version:       2.1.0
Release:       3%{?dist}
Summary:       Simple command line mail merge tool

License:       MIT
URL:           https://github.com/awdeorio/mailmerge
Source0:       %{pypi_source}
# https://github.com/awdeorio/mailmerge/pull/91
Patch0: configparser.patch
BuildArch:     noarch

%description
%{summary}.

%package -n python3-%{srcname}
Summary:       %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Provides:      %{srcname} = %{version}-%{release}
BuildRequires: python3-devel

%description -n python3-%{srcname}
%{summary}.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -vr *.egg-info

%build
%{py3_build}

%install
%{py3_install}

%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{_bindir}/mailmerge
%{python3_sitelib}/mailmerge/
%{python3_sitelib}/mailmerge-*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-3
- Rebuilt for Python 3.9

* Wed Apr 29 2020 Brian Exelbierd <bexelbie@redhat.com> - 2.1-1
- Remove configparser dependency

* Thu Apr 23 2020 Brian Exelbierd <bexelbie@redhat.com> - 2.1-1
- Update to 2.1.0
- remove merged patch

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 19 2019 Brian Exelbierd <bexelbie@redhat.com> - 1.9-2
- Adding Patch for F30 backports-csv drop

* Thu May 16 2019 Brian Exelbierd <bexelbie@redhat.com> - 1.9-1
- Initial package
