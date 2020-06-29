%global         srcname yaspin
Name:           python-yaspin
Version:        0.14.3
Release:        6%{?dist}
License:        MIT
URL:            https://pypi.org/project/yaspin
Source0:        https://github.com/pavdmyt/yaspin/archive/v%{version}.tar.gz
BuildArch:      noarch
Summary:        Python library for terminal spinners
%description
Yet Another Terminal Spinner for Python.

Yaspin provides a full-featured terminal spinner to show the progress
during long-hanging operations.

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Yet Another Terminal Spinner for Python.

Yaspin provides a full-featured terminal spinner to show the progress
during long-hanging operations.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
# some tests are skipped because they are generated, some combinations are not supported use cases
#example: tests/test_in_out.py::test_compose_out_with_color[None-''-bold] SKIPPED
%{__python3} -m pytest

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.14.3-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 2019 Patrik Kopkan <pkopkan@redhat.com> - 0.14.3-1
- update for 0.14.3

* Mon Jan 14 2019 Patrik Kopkan <pkopkan@redhat.com> - 0.14.0-4
- fixed typo

* Fri Jan 11 2019 Patrik Kopkan <pkopkan@redhat.com> - 0.14.0-4
- added BuildRequires
- changed tabs to spaces

* Thu Jan 10 2019 Patrik Kopkan <pkopkan@redhat.com> - 0.14.0-3
- fixed typo
- deleted Requires

* Wed Jan 9 2019 Patrik Kopkan <pkopkan@redhat.com> - 0.14.0-2
- added BuildRequires

* Tue Jan 8 2019 Patrik Kopkan <pkopkan@redhat.com> - 0.14.0-1
- created package
