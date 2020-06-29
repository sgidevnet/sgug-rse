# Use a git commit with fixes
%global commit 827b609e61c5821347ad06e865c86722c11fe9f3
%global shortcommit %(c=%{commit}; echo ${c:0:7})

# Multiple tests fail on i386
# https://github.com/nipy/nitime/issues/136
# https://github.com/nipy/nitime/issues/137
%bcond_with tests

# Docs are broken, need to be reported upstream
# Currently disabled
%bcond_with docs


%global srcname nitime

%global _description %{expand:
Nitime is library of tools and algorithms for the analysis of time-series data
from neuroscience experiments. It contains a implementation of numerical
algorithms for time-series analysis both in the time and spectral domains, a
set of container objects to represent time-series, and auxiliary objects that
expose a high level interface to the numerical machinery and make common
analysis tasks easy to express with compact and semantically clear code.

Current information can always be found at the nitime website. Questions and
comments can be directed to the mailing list:
http://mail.scipy.org/mailman/listinfo/nipy-devel.

Documentation is available at http://nipy.org/nitime/documentation.html
}


Name:           python-%{srcname}
Version:        0.8.1
Release:        6%{?dist}
Summary:        Timeseries analysis for neuroscience data

License:        BSD
URL:            http://nipy.org/%{srcname}
Source0:        https://github.com/nipy/nitime/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz
Patch0:         0001-Remove-six.patch

BuildRequires:  python3-devel

BuildRequires:  %{py3_dist cython}
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist networkx}
BuildRequires:  %{py3_dist nibabel}
BuildRequires:  %{py3_dist nose}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  gcc
BuildRequires:  git-core

Requires:       %{py3_dist numpy}
Requires:       %{py3_dist scipy}
Requires:       %{py3_dist matplotlib}
Requires:       %{py3_dist networkx}
Requires:       %{py3_dist nibabel}
Requires:       %{py3_dist cython}
Requires:       %{py3_dist six}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%if %{with docs}
%package doc
Summary:    Documentation for %{name}
BuildArch:  noarch

# Bundles a few sphinxexts but they don't seem to be easy to find
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist numpydoc}
BuildRequires:  texlive-latex
BuildRequires:  texlive-ucs
BuildRequires:  tex(amsthm.sty)

%description doc
Documentation files for %{name}.
%endif

%prep
%autosetup -n %{srcname}-%{commit} -S git
rm -rvf %{srcname}.egg-info
rm -f nitime/six.py

find . -name "*.so" -exec rm -fv '{}' \;

# Correct shebangs to python3
sed -i 's|^#!/usr/bin/env python|#!/usr/bin/python3|' setup.py
sed -i 's|python|python3|' doc/Makefile

# This example doesn't seem to be correct, so we remove it for the time being and let upstream know.
rm -fv doc/examples/filtering_fmri.py

pushd tools
    for f in *; do
        sed -E -i 's|^#!/usr/bin/env python|#!/usr/bin/python3|' "$f"
    done
popd

%build
%py3_build

%if %{with docs}
pushd doc &&
    PYTHONPATH=../ make html &&
    rm -fv _build/html/.buildinfo
popd
%endif


%install
%py3_install

%check
%if %{with tests}
# From https://github.com/neurodebian/nitime/blob/3ca5a131ba1ea839e047a7a2e008b754be9fe4bb/debian/rules#L47
PYTHONPATH=$RPM_BUILD_ROOT/%{python3_sitearch} nosetests-3 '--exclude=test_(coherence_linear_dependence|lazy_reload)' nitime
%endif

%files -n python3-%{srcname}
%license LICENSE
%doc README.txt THANKS
%{python3_sitearch}/%{srcname}-%{version}-py%{python3_version}.egg-info
%{python3_sitearch}/%{srcname}

%if %{with docs}
%files doc
%license LICENSE
%doc doc/_build/html
%endif

%changelog
* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.1-6
- Explicitly BR setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-2
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.1-1
- Update to new version
- Fix build
- Use conditionals
- Drop Python 2
- Disable broken doc build

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-0.4.git1fab571
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-0.3.git1fab571
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 06 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8-0.2.git1fab571
- Enable documentation on rawhide where build succeeds (F30)
- Remove extra buildinfo file
- Make doc package noarch
- Move THANKS file to correct bits

* Sun Nov 04 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8-0.1.git1fab571
- Initial build
