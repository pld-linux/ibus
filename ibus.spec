#
# Conditional build:
%bcond_without	gjsfile		# https://bugzilla.redhat.com/show_bug.cgi?id=657165
#
Summary:	Intelligent Input Bus for Linux OS
Name:		ibus
Version:	1.3.99.20110419
Release:	1
License:	LGPL v2+
Group:		Libraries
URL:		http://code.google.com/p/ibus/
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	d4f2729fecb92ae6b41f26c770b1a772
Source1:	%{name}.xinputd
Source100:	http://fujiwara.fedorapeople.org/ibus/gnome-shell/%{name}-gjs-1.3.99.20110714.tar.gz
# Source100-md5:	57df6a7d6a9ca0f4b30a8fe135fdcb89
Patch0:		%{name}-HEAD.patch
Patch1:		%{name}-530711-preload-sys.patch
Patch2:		%{name}-xx-icon-symbol.patch
Patch3:		%{name}-541492-xkb.patch
Patch4:		%{name}-xx-bridge-hotkey.patch
Patch5:		%{name}-xx-setup-frequent-lang.patch
# Workaround for oxygen-gtk icon theme until bug 699103 is fixed.
Patch91:	%{name}-711632-fedora-fallback-icon.patch
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	iso-codes
BuildRequires:	libtool
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.596
BuildRequires:	rpm-pythonprov
BuildRequires:	python-dbus-devel >= 0.83.0
BuildRequires:	python-pygobject-devel
BuildRequires:	xorg-lib-libxkbfile-devel
Requires:	%{name}-gtk2 = %{version}-%{release}
Requires:	%{name}-gtk3 = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	GConf2
Requires:	im-chooser
Requires:	iso-codes
Requires:	python-dbus >= 0.83.0
Requires:	python-pygtk-gtk
Requires:	python-pynotify
Requires:	python-pyxdg
Requires:	hicolor-icon-theme
Requires:	gtk-update-icon-cache
# input-keyboard-symbolic icon
Suggests:	gnome-icon-theme-symbolic
Requires(post):	GConf2
Requires(preun):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
IBus means Intelligent Input Bus. It is an input framework for Linux
OS.

%package libs
Summary:	IBus libraries
Group:		Libraries
Requires:	dbus >= 1.2.4
Requires:	glib2 >= 1:2.26.0

%description libs
This package contains the libraries for IBus

%package gtk2
Summary:	IBus im module for gtk2
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	imsettings-gnome2
Requires(post):	glib2 >= 1:2.26.0

%description gtk2
This package contains ibus im module for gtk2

%package gtk3
Summary:	IBus im module for gtk3
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	imsettings-gnome3
Requires(post):	glib2 >= 1:2.26.0

%description gtk3
This package contains ibus im module for gtk3

%package gnome3
Summary:	IBus gnome-shell-extension for GNOME3
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gnome-shell

%description gnome3
This is a transitional package which allows users to try out new IBus
GUI for GNOME3 in development. Note that this package will be marked
as obsolete once the integration has completed in the GNOME3 upstream.

%package devel
Summary:	Development tools for ibus
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus-devel
Requires:	glib2-devel

%description devel
The ibus-devel package contains the header files and developer docs
for ibus.

%prep
%setup -q
%if %{with gjsfile}
zcat %SOURCE100 | tar xf -
%endif
%patch0 -p1
cp client/gtk2/ibusimcontext.c client/gtk3/ibusimcontext.c
%patch1 -p1
%patch2 -p1
%patch3 -p1
mv data/ibus.schemas.in data/ibus.schemas.in.in
%patch4 -p1
%patch5 -p1

%patch91 -p1

%build
%if %{with gjsfile}
d=`basename %SOURCE100 .tar.gz`
cd $d
%configure
%{__make}
cd ..
%endif

%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk2 \
	--enable-gtk3 \
	--enable-xim \
	--enable-vala \
	--enable-xkb \
	--disable-gtk-doc \
	--enable-gconf \
	--enable-python \
	--with-html-dir=%{_gtkdocdir} \
	--with-no-snooper-apps='gnome-do,Do.*,firefox.*,.*chrome.*,.*chromium.*' \
	--enable-surrounding-text \
	--enable-bridge-hotkey \
	--enable-introspection

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{X11/xinit/xinput.d,xdg/autostart}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__sed} -e 's|@@LIB@@|%{_lib}|g' %{SOURCE1} >$RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinput.d/ibus.conf

# correct location in upstream.
mv $RPM_BUILD_ROOT{%{_desktopdir},%{_sysconfdir}/xdg/autostart}/ibus.desktop

%if %{with gjsfile}
d=`basename %SOURCE100 .tar.gz`
cd $d
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%{__rm} $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/ibus-gjs.mo
cd ..
%endif

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk*/*/immodules/*.la

%find_lang %{name}10

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%gconf_schema_install ibus.schemas

%preun
%gconf_schema_uninstall ibus.schemas

%postun
%update_icon_cache hicolor

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%post gtk2
%if "%{_lib}" != "lib"
%{_bindir}/gtk-query-immodules-2.0-64 > %{_sysconfdir}/gtk64-2.0/gtk.immodules
%else
%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules
%endif

%postun gtk2
%if "%{_lib}" != "lib"
%{_bindir}/gtk-query-immodules-2.0-64 > %{_sysconfdir}/gtk64-2.0/gtk.immodules
%else
%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules
%endif

%post gtk3
%if "%{_lib}" != "lib"
%{_bindir}/gtk-query-immodules-3.0-64 --update-cache
%else
%{_bindir}/gtk-query-immodules-3.0 --update-cache
%endif

%postun gtk3
%if "%{_lib}" != "lib"
%{_bindir}/gtk-query-immodules-3.0-64 --update-cache
%else
%{_bindir}/gtk-query-immodules-3.0 --update-cache
%endif

%files -f %{name}10.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%config %{_sysconfdir}/X11/xinit/xinput.d/ibus.conf
# imsettings will start this daemon for us
#%{_sysconfdir}/xdg/autostart/ibus.desktop
%{_sysconfdir}/gconf/schemas/ibus.schemas
%attr(755,root,root) %{_bindir}/ibus-daemon
%attr(755,root,root) %{_bindir}/ibus-setup
%attr(755,root,root) %{_libexecdir}/ibus-gconf
%attr(755,root,root) %{_libexecdir}/ibus-ui-gtk
%attr(755,root,root) %{_libexecdir}/ibus-x11
%attr(755,root,root) %{_libexecdir}/ibus-engine-xkb
%attr(755,root,root) %{_libexecdir}/ibus-xkb
%dir %{py_sitescriptdir}/ibus
%{py_sitescriptdir}/ibus/*
%{_datadir}/ibus
%{_desktopdir}/*
%{_iconsdir}/hicolor/*/apps/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libibus-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libibus-1.0.so.[0-9]
%{_libdir}/girepository-1.0/IBus-1.0.typelib

%files gtk2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.0/*/immodules/im-ibus.so

%files gtk3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-3.0/*/immodules/im-ibus.so

%files gnome3
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/js/ui/status/ibus
%{_datadir}/gnome-shell/extensions/ibus-indicator@example.com

%files devel
%defattr(644,root,root,755)
%doc %{_gtkdocdir}/ibus
%attr(755,root,root) %{_libdir}/lib*.so
%{_pkgconfigdir}/ibus-1.0.pc
%{_includedir}/ibus-1.0
%{_datadir}/gir-1.0/IBus-1.0.gir
%{_datadir}/vala/vapi/ibus-1.0.vapi
%{_datadir}/vala/vapi/ibus-1.0.deps
