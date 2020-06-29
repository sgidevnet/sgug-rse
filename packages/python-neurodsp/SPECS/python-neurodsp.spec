%bcond_without tests

%global pypi_name neurodsp

%global _description %{expand:
NeuroDSP is package of tools to analyze and simulate neural 
time series, using digital signal processing.

Available modules in NeuroDSP include:

* filt : Filter data with bandpass, highpass, lowpass, or
notch filters
* burst : Detect bursting oscillations in neural signals
* rhythm : Find and analyze rhythmic and recurrent patterns
in time series
* spectral : Compute spectral domain features such as power
spectra
* timefrequency : Estimate instantaneous measures of
oscillatory activity
* sim : Simulate time series, including periodic and
aperiodic signal components
* plts : Plotting functions

If you use this code in your project, please cite:

Cole, S., Donoghue, T., Gao, R., & Voytek, B. (2019).
NeuroDSP: A package for neural digital signal processing.
Journal of Open Source Software, 4(36), 1272.
https://doi.org/10.21105/joss.01272}

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        5%{?dist}
Summary:        A tool for digital signal processing for neural time series

License:        ASL 2.0
URL:            https://neurodsp-tools.github.io/
Source0:        https://github.com/neurodsp-tools/%{pypi_name}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
Patch1:			0001-Enforce-that-wavelet_len-be-an-int-as-it-should-be.patch

BuildArch:      noarch

# Install dependencies automatically
%{?python_enable_dependency_generator}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist matplotlib}

%if %{with tests}
BuildRequires:  python3-pytest
%endif

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%prep
# No keyring/signature from the upstream to verify the source
%autosetup -n %{pypi_name}-%{version} -p1
rm -rf %{pypi_name}.egg-info

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build
# cannot build the docs, as it downloads additional datasets (through mne).
# the docs also don't build unless line #101 is uncommented (in conf.py).

%install
%py3_install

%check
%if %{with tests}
pytest-3
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md paper/*
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}

%changelog
* Thu Jun 25 2020 Aniket Pradhan <major AT fedoraproject DOT org> - 2.0.0-5
- Added setuptools to BuildRequires

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-4
- Rebuilt for Python 3.9

* Sat Feb 08 2020 Aniket Pradhan <major AT fedoraproject DOT org> - 2.0.0-3
- Removed gnupg from BuildRequires
- Added a patch to fix some test failures

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 11 2019 Aniket Pradhan <major AT fedoraproject DOT org> - 2.0.0-1
- Initial build
